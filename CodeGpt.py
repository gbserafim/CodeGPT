import os
import streamlit as st 
from groq import Groq
st.set_page_config(
    page_title="CodeGPT - Seu Assistente de Programação",
    layout="wide",
    initial_sidebar_state="expanded"
)
CUSTOM_PROMPT = """
Você é um programador especialista em Python, JavaScript, HTML, CSS, PHP, SQL, Java, C#, Ruby, Swift, Go, TypeScript e outras linguagens de programação. Você é capaz de entender requisitos complexos e gerar código eficiente e funcional. Você também pode explicar conceitos de programação e ajudar a resolver problemas técnicos.

Regras:
1. Sempre escreva código limpo e bem documentado.
2. Use boas práticas de programação.
3. Teste o código antes de entregá-lo.
4. Se o pedido for vago, peça mais detalhes.
5. Nunca escreva código malicioso ou que viole direitos autorais.
6. Sempre explique o código que você gera.
7. Se o pedido for para criar um projeto, forneça uma estrutura de diretórios.
8. Se o pedido for para corrigir um erro, explique a causa do erro e como corrigi-lo.
9. Se o pedido for para otimizar o código, explique as melhorias feitas.
10. Se o pedido for para aprender uma nova linguagem ou tecnologia, forneça recursos úteis.
11. Sempre mantenha a ética profissional e o respeito pelo usuário.
12. Nunca compartilhe informações pessoais ou sensíveis.
13. Se o pedido for para criar um script automatizado, explique como ele funciona e quais são os riscos envolvidos.
14. Se o pedido for para criar uma aplicação web, explique as tecnologias usadas e como garantir a segurança.
15. Se o pedido for para criar uma API, explique os endpoints e como usá-los
16. Se o pedido for para criar um banco de dados, explique o modelo de dados e como garantir a integridade dos dados.
17. Se o pedido for para criar um aplicativo móvel, explique as plataformas suportadas e como garantir a performance.
18. Se o pedido for para criar um jogo, explique a mecânica do jogo e como garantir a diversão.
19. Se o pedido for para criar um sistema de aprendizado de máquina, explique os algoritmos usados e como garantir a precisão.
20. Se o pedido for para criar um sistema de inteligência artificial, explique os modelos usados e como garantir a ética.
"""

with st.sidebar: 
    st.title("CodeGPT")
    st.markdown("Seu Assistente de Programação")
    groq_api_key = st.text_input("Insira sua Groq API Key:", type="password")
    if not groq_api_key:
        st.warning("Por favor, insira sua Groq API Key para continuar.")
        st.stop()
    st.markdown("---")
    st.markdown("## Sobre")
    st.markdown("CodeGPT é um assistente de programação alimentado por IA que ajuda desenvolvedores a escrever, depurar e entender código em várias linguagens de programação.")
    st.markdown("## Instruções")
    st.markdown(
        "1. Insira sua Groq API Key na barra lateral.\n"
        "2. Digite sua pergunta ou solicitação relacionada à programação na caixa de texto abaixo.\n"
        "3. Clique em 'Enviar' e aguarde a resposta do CodeGPT.\n"
        "4. Revise o código gerado ou as explicações fornecidas."
    )
    st.markdown("## Linguagens Suportadas")
    st.markdown("- Python\n- JavaScript\n- HTML/CSS\n- PHP\n- SQL\n- Java\n- C#\n- Ruby\n- Swift\n- Go\n- TypeScript")
    st.markdown("-----")
    st.markdown("## Contato")
    st.markdown("Desenvolvido por Gabriel Monteiro ([dev.gb99@gmail.com](mailto:dev.gb99@gmail.com))")

st.title("CodeGPT - Seu Assistente de Programação")
user_input = st.text_area("Digite sua pergunta ou solicitação relacionada à programação:", height=200)
if st.button("Enviar"):
    if not user_input.strip():
        st.warning("Por favor, insira uma pergunta ou solicitação.")
    else:
        with st.spinner("Processando sua solicitação..."):
            groq = Groq(api_key=groq_api_key)
            prompt = f"{CUSTOM_PROMPT}\n\nUsuário: {user_input}\nCodeGPT:"
            try:
                response = groq.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": CUSTOM_PROMPT},
                        {"role": "user", "content": user_input}
                    ],
                    max_tokens=1000,
                    temperature=0.2,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0,
                )
                answer = response.choices[0].message['content']
                st.markdown("### Resposta do CodeGPT:")
                st.code(answer, language='answer')
            except Exception as e:
                st.error(f"Ocorreu um erro ao processar sua solicitação: {e}")

st.markdown("---")