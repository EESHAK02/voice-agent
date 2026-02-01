from components.llm import generate_response
def test_llm_generates_response():
    history = []
    response = generate_response("Hello", history)

    assert isinstance(response, str)
    assert len(response) > 0
