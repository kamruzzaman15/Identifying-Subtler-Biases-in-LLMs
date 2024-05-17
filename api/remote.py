from litellm import completion
import litellm
litellm.set_verbose=True

def generate_response_api(model: str, query: str) -> str:
    response = completion(
            model=model, 
            temperature=0,
            max_tokens=50,
            messages = [{ "content": query,"role": "user"}]
        )

    return response.choices[0].message.content