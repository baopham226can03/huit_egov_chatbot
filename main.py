import yaml
from src.subbots.subbot import SubBot
from src.masterbot.router import MasterBot

def main():
    # Load subbots from config
    with open("bots_config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    subbots = {
        bot["name"]: SubBot(bot["name"], bot["data_path"], bot["collection_name"])
        for bot in config["bots"]
    }
    # print(f"Debug - Subbots initialized: {list(subbots.keys())}")

    # Initialize masterbot
    masterbot = MasterBot(subbots)

    # User query loop
    while True:
        query = input("Nhập câu hỏi (hoặc 'exit' để thoát): ")
        if query.lower() == "exit":
            break

        response, category = masterbot.process_query(query)
        # print(f"\n🧠 Phân hệ: {category}")
        print(f"{response}")

if __name__ == "__main__":
    main()