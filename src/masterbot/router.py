from openai import OpenAI
from src.common.config import Config

class MasterBot:
    def __init__(self, subbots):
        self.subbots = subbots
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)

    def classify_query(self, query):
        prompt = f"""
        Bạn là một trợ lý AI chuyên phân loại câu hỏi tiếng Việt. Dựa trên câu hỏi dưới đây, hãy xác định nó thuộc danh mục nào trong số các danh mục sau: 
        '{', '.join(self.subbots.keys())}'.
        
        Chỉ trả về tên danh mục phù hợp nhất, hoặc 'unknown' nếu không xác định được.
        Đảm bảo tên danh mục khớp chính xác với danh sách trên, không thêm khoảng trắng thừa hoặc ký tự không cần thiết.

        Câu hỏi: "{query}"
        """
        response = self.client.chat.completions.create(
            model=Config.LLM_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        category = response.choices[0].message.content.strip()
        return category

    def process_query(self, query):
        category = self.classify_query(query)
        # print(f"Debug - Category from LLM: '{category}'")
        # print(f"Debug - Available subbots: {list(self.subbots.keys())}")
        
        if category in self.subbots:
            response = self.subbots[category].process_query(query)
            return response, category
        else:
            # Khi không xác định được phân hệ, trả về thông báo thân thiện và liệt kê các phân hệ
            available_categories = ", ".join(self.subbots.keys())
            response = (f"Vui lòng cung cấp câu hỏi cụ thể hơn để tôi có thể hỗ trợ tốt nhất! "
                       f"Các chủ đề sẵn sàng hỗ trợ: {available_categories}.")
            return response, "unknown"