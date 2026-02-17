from google import genai
client=genai.Client(api_key="AIzaSyCzRI8pOuzfFNDr8zBLWfao-cV5D3eIuwM")
chat=client.chats.create(model="gemini-3-flash-preview")
response=chat.send_message("k xa")
print("GEMINI:",response.text)
while True:
    user_input=input("YOU: ")
    if user_input.lower()=="exit":
        print("GOODBYE")
        break
    response=chat.send_message(user_input)
    print("GEMMINI: ",response.text)