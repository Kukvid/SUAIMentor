async function getResponse(){
    let response = await fetch("http://127.0.0.1:8000/todos")
    let content = await response.json()
    return content
}