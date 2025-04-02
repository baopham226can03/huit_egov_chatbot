# HUIT eGov Chatbot

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green) ![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Store-orange) ![License](https://img.shields.io/badge/License-MIT-yellow)

**HUIT eGov Chatbot** là một trợ lý AI thông minh được thiết kế để hỗ trợ người dùng sử dụng hệ thống HUIT eGov. Dự án tích hợp Retrieval-Augmented Generation (RAG) với OpenAI API và ChromaDB để cung cấp câu trả lời chính xác dựa trên tài liệu hướng dẫn, đồng thời hỗ trợ truy xuất dữ liệu cá nhân thông qua function calling.

## Mục tiêu dự án

- **Hỗ trợ người dùng**: Cung cấp hướng dẫn chi tiết về cách sử dụng hệ thống HUIT eGov thông qua giao tiếp tự nhiên.
- **Tích hợp RAG**: Sử dụng tài liệu PDF hướng dẫn để trả lời câu hỏi, kết hợp với khả năng truy xuất dữ liệu cá nhân (ví dụ: lịch cá nhân).
- **Dễ mở rộng**: Thiết kế mô-đun hóa để dễ dàng thêm tính năng hoặc tích hợp với các API thực tế của HUIT eGov.

## Tính năng chính

1. **Truy xuất thông tin từ tài liệu**:
   - Tự động xử lý và lưu trữ nội dung PDF hướng dẫn vào vector store.
   - Truy xuất nội dung liên quan dựa trên câu hỏi của người dùng.
2. **Function Calling**:
   - Hỗ trợ gọi các hàm để lấy dữ liệu cá nhân (hiện tại giả lập với `get_user_schedule`).
3. **Giao tiếp thông minh**:
   - Sử dụng mô hình `gpt-4o-mini` của OpenAI để tạo câu trả lời tự nhiên và chính xác.
4. **Xử lý văn bản lớn**:
   - Chia nhỏ nội dung PDF thành các chunk để tránh vượt giới hạn token của OpenAI API.

## Cấu trúc dự án
huit_egov_chatbot/
│
├── data/                    # Thư mục chứa các file PDF hướng dẫn
│   ├── guide1.pdf          # Ví dụ file PDF
│   └── ...
│
├── src/                    # Thư mục chứa mã nguồn
│   ├── init.py        # Khởi tạo package
│   ├── config.py          # Cấu hình và load biến môi trường
│   ├── vector_store.py    # Quản lý vector database (ChromaDB)
│   ├── pdf_processor.py   # Xử lý và embedding PDF
│   ├── functions.py       # Định nghĩa các hàm function calling
│   └── chatbot.py         # Logic chính của chatbot
│
├── .env                    # File chứa biến môi trường (không commit lên git)
├── main.py                 # File chạy chính
├── requirements.txt        # Danh sách thư viện cần cài đặt
└── README.md               # Tài liệu hướng dẫn (bạn đang đọc)

### Chi tiết các file

- **`main.py`**: Điểm khởi đầu của ứng dụng, khởi tạo các thành phần và chạy vòng lặp chatbot.
- **`src/config.py`**: Load biến môi trường từ `.env` (API key, model, index name).
- **`src/vector_store.py`**: Quản lý ChromaDB để lưu trữ và truy xuất embeddings.
- **`src/pdf_processor.py`**: Đọc PDF, chia nhỏ nội dung, tạo embeddings và lưu vào vector store.
- **`src/functions.py`**: Định nghĩa các hàm function calling (hiện có `get_user_schedule`).
- **`src/chatbot.py`**: Xử lý câu hỏi người dùng, tích hợp RAG và function calling.

## Yêu cầu hệ thống

- **Python**: 3.8 trở lên
- **Hệ điều hành**: Windows, macOS, Linux
- **Kết nối internet**: Để gọi OpenAI API
- **Dung lượng**: Tối thiểu 1GB RAM, 500MB ổ cứng (tùy thuộc vào số lượng PDF)

## Cài đặt

### 1. Clone repository
```bash
git clone https://github.com/yourusername/huit_egov_chatbot.git
cd huit_egov_chatbot

### 2. Tạo file .env

Tạo file `.env` trong thư mục gốc với nội dung sau (thay bằng giá trị thực tế của bạn):

```ini
OPENAI_API_KEY=your-openai-api-key
LLM_MODEL=gpt-4o-mini
INDEX_NAME=huit_egov
```

- `OPENAI_API_KEY`: Khóa API từ OpenAI (bắt buộc).
- `LLM_MODEL`: Mô hình LLM, mặc định là `gpt-4o-mini`.
- `INDEX_NAME`: Tên collection trong ChromaDB, phải từ 3-63 ký tự (ví dụ: `huit_egov`).

### 3. Cài đặt thư viện

Chạy lệnh sau để cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
```

Các thư viện bao gồm:

- `openai`: Gọi API OpenAI.
- `chromadb`: Vector database.
- `PyPDF2`: Đọc file PDF.
- `python-dotenv`: Load biến môi trường.
- `tqdm`: Thanh tiến trình.

### 4. Chuẩn bị dữ liệu

- Đặt các file PDF hướng dẫn vào thư mục `data/`.
- Đảm bảo ít nhất một file PDF tồn tại để chatbot có dữ liệu xử lý.

## Cách sử dụng

### Chạy chương trình

```bash
python main.py
```

Chương trình sẽ:

1. Xử lý tất cả PDF trong thư mục `data/`, chia nhỏ và lưu vào ChromaDB.
2. Hiển thị prompt để bạn nhập câu hỏi.

### Ví dụ tương tác

```text
Processing PDFs: 100%|██████████| 1/1 [00:07<00:00,  7.45s/it]
Processed and stored 6 chunks from PDFs.

Nhập câu hỏi (hoặc 'exit' để thoát): Đăng nhập thế nào ạ
Chatbot: Để đăng nhập vào hệ thống HUIT eGov, bạn cần làm theo các bước sau: [dựa trên nội dung PDF].

Nhập câu hỏi (hoặc 'exit' để thoát): Lịch của tôi hôm nay là gì
Chatbot: Lịch hôm nay của bạn: 09:00 - Họp nhóm, 14:00 - Gửi báo cáo.

Nhập câu hỏi (hoặc 'exit' để thoát): exit
```

## Quy trình hoạt động

1. **User Prompt**: Người dùng nhập câu hỏi (ví dụ: "Đăng nhập thế nào ạ").
2. **Backend**:
   - Embedding câu hỏi bằng `text-embedding-ada-002`.
   - Truy xuất 3 đoạn nội dung liên quan nhất từ ChromaDB.
   - Gửi câu hỏi, system prompt, nội dung truy xuất và danh sách hàm đến `gpt-4o-mini`.
   - Nếu cần, gọi hàm (ví dụ: `get_user_schedule`) và gửi kết quả trở lại model.
   - Model tạo câu trả lời cuối cùng.
3. **Trả lời**: Chatbot hiển thị câu trả lời cho người dùng.

## Tùy chỉnh và mở rộng

### Thêm hàm mới

Mở `src/functions.py`, thêm định nghĩa hàm vào `FUNCTIONS`:

```python
{
    "type": "function",
    "function": {
        "name": "get_user_info",
        "description": "Lấy thông tin người dùng",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {"type": "string", "description": "ID của người dùng"}
            },
            "required": ["user_id"]
        }
    }
}
```

Thêm logic thực thi trong `execute_function`:

```python
if function_name == "get_user_info":
    return {"user_id": arguments["user_id"], "name": "Nguyen Van A"}
```

### Tích hợp API thực tế

Thay hàm giả lập trong `src/functions.py` bằng API của HUIT eGov:

```python
import requests

def get_user_schedule(user_id):
    response = requests.get(f"https://huit-egov-api.com/schedule/{user_id}")
    return response.json()
```

### Thay đổi mô hình embedding

Trong `.env`, thêm `EMBEDDING_MODEL` (ví dụ: `VoVanPhuc/sup-SimCSE-VietNamese-phobert-base`) và cập nhật `src/pdf_processor.py` để dùng mô hình này (yêu cầu tích hợp Hugging Face).

## Xử lý lỗi thường gặp

- **`ModuleNotFoundError`**: Kiểm tra `pip install -r requirements.txt` đã chạy thành công.
- **`ValueError: Expected collection name...`**: Đảm bảo `INDEX_NAME` trong `.env` từ 3-63 ký tự (ví dụ: `huit_egov`).
- **`openai.BadRequestError: maximum context length`**: Đảm bảo `pdf_processor.py` chia nhỏ nội dung PDF đúng cách.
- **`openai.BadRequestError: Missing tools[0].type`**: Kiểm tra `FUNCTIONS` trong `src/functions.py` có trường `"type": "function"`.

## Hiệu suất và tối ưu hóa

- **Thời gian xử lý PDF**: Phụ thuộc vào kích thước file và số chunk (ví dụ: ~7.45s cho 1 PDF).
- **Tối ưu hóa**:
  - Giảm `max_tokens` trong `pdf_processor.py` để tạo nhiều chunk nhỏ hơn, tăng độ chính xác truy xuất.
  - Lưu trữ vector store trên đĩa bằng `chromadb.PersistentClient` thay vì RAM.

## Đóng góp

1. Fork repository.
2. Tạo branch mới:
   
   ```bash
   git checkout -b feature/your-feature
   ```

3. Commit thay đổi:
   
   ```bash
   git commit -m "Add your feature"
   ```

4. Push lên branch:
   
   ```bash
   git push origin feature/your-feature
   ```

5. Tạo Pull Request.

