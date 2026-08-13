class ContextBuilder:

    def build(self, results) -> str:

        contexts = []

        for result in results:

            payload = result.payload

            contexts.append(
                (
                    f"[Page {payload['page']}]\n"
                    f"{payload['text']}"
                )
            )

        return "\n\n---\n\n".join(contexts)