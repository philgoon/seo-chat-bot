import openai
import streamlit as st

# Set your OpenAI API key here
openai.api_key = "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"  # Replace with your actual API key

def display_existing_messages():
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def add_user_message_to_session(prompt):
    if prompt:
        st.session_state["messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

def generate_nickname(prompt):
    if prompt:
        system_prompt = (
            "Brazilian Name Bot, designed to generate unique Brazilian-style soccer nicknames, "
            "always operates in English. It emphasizes creating deeply personal and resonant nicknames "
            "by prompting users to share unique attributes about themselves. This approach ensures each "
            "nickname is tailored to the individual, drawing from their characteristics and blending them "
            "with the flair of Brazilian soccer legends like Pelé and Ronaldo. The GPT offers three nickname "
            "suggestions, each accompanied by a brief, imaginative backstory. If faced with a challenging name "
            "or insufficient information, it respectfully requests more details, ensuring the nicknames are as "
            "personalized and meaningful as possible. It upholds a playful, engaging tone while being culturally "
            "sensitive and reflective of the legendary Brazilian soccer spirit. Generated names must be one word."
        )

        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']

def main():
    st.title("Brazilian Legend Name Crafter")
    st.write("Generate your unique Brazilian-style soccer nickname!")

    display_existing_messages()

    user_input = st.chat_input("Enter your characteristics:")
    if user_input:
        add_user_message_to_session(user_input)
        nickname = generate_nickname(user_input)
        st.session_state["messages"].append({"role": "assistant", "content": nickname})
        with st.chat_message("assistant"):
            st.markdown(nickname)

if __name__ == "__main__":
    main()

