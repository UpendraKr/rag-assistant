from app.db.qdrant import create_collection


if __name__ == "__main__":
    create_collection()
    print("Qdrant collection initialized")