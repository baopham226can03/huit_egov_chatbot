import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.chatbot import Chatbot
from src.pdf_processor import PDFProcessor
from src.vector_store import VectorStore


def main():
    # Khởi tạo các thành phần
    data_dir = "data"
    vector_store = VectorStore()
    pdf_processor = PDFProcessor(vector_store)

    # Tải và xử lý tất cả PDF trong thư mục data
    pdf_processor.process_pdfs(data_dir)

    # Khởi tạo chatbot
    chatbot = Chatbot(vector_store)

    # Vòng lặp thử nghiệm chatbot
    while True:
        user_input = input("Nhập câu hỏi (hoặc 'exit' để thoát): ")
        if user_input.lower() == "exit":
            break
        response = chatbot.handle_query(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()