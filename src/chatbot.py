from openai import OpenAI
from src.config import Config
from src.vector_store import VectorStore
from src.functions import FUNCTIONS, execute_function

class Chatbot:
    def __init__(self, vector_store: VectorStore):
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        self.vector_store = vector_store
        self.system_prompt = """
        Bạn là một trợ lý AI hỗ trợ người dùng sử dụng hệ thống HUIT eGov. 
        Dựa trên tài liệu hướng dẫn và dữ liệu cá nhân (nếu cần), hãy trả lời câu hỏi của người dùng một cách chính xác, ngắn gọn và hữu ích.
        """

    def get_embedding(self, text):
        response = self.client.embeddings.create(
            model="text-embedding-ada-002",
            input=text
        )
        return response.data[0].embedding

    def handle_query(self, user_prompt):
        # 1. Embedding user prompt
        query_embedding = self.get_embedding(user_prompt)

        # 2. Truy xuất nội dung hướng dẫn từ vector store
        relevant_docs = self.vector_store.query(query_embedding, n_results=3)
        context = "\n".join(relevant_docs)

        # 3. Gửi yêu cầu tới model với context và function list
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": f"{user_prompt}\n\nHướng dẫn liên quan:\n{context}"}
        ]
        response = self.client.chat.completions.create(
            model=Config.LLM_MODEL,
            messages=messages,
            tools=FUNCTIONS,
            tool_choice="auto"
        )


        # 4. Kiểm tra xem model có yêu cầu gọi hàm không
        tool_calls = response.choices[0].message.tool_calls
        if tool_calls:
            for tool_call in tool_calls:
                function_result = execute_function({
                    "name": tool_call.function.name,
                    "arguments": tool_call.function.arguments
                })
                # 6. Gửi kết quả hàm trở lại model
                messages.append({
                    "role": "assistant",
                    "tool_calls": [
                        {
                            "id": tool_call.id,
                            "type": "function",
                            "function": {
                                "name": tool_call.function.name,
                                "arguments": tool_call.function.arguments
                            }
                        }
                    ]
                })
                messages.append({
                    "role": "tool",
                    "name": tool_call.function.name,
                    "tool_call_id": tool_call.id,  # Thêm tool_call_id vào đây
                    "content": str(function_result)
                })



                final_response = self.client.chat.completions.create(
                    model=Config.LLM_MODEL,
                    messages=messages
                )
                return final_response.choices[0].message.content

        # 7. Trả về câu trả lời nếu không cần gọi hàm
        return response.choices[0].message.content
