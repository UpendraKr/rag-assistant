def get_document_key(document):

    metadata = document.metadata

    return (
        metadata.get("document_id"),
        metadata.get("chunk_index"),
    )


def deduplicate_documents(documents):

    unique = {}

    for document in documents:

        key = get_document_key(
            document
        )

        if key not in unique:

            unique[key] = document

    return list(unique.values())