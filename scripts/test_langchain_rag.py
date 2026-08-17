from app.chains.rag_chain import rag_chain


question = "What is ranking of iit delhi in 2021 for engineering?"


answer = rag_chain.invoke(
    question
)


print("\nANSWER:")
print(answer)