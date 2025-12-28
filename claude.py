import anthropic

messages = []
system = '''
   Keep replies under 400 words unless otherwise needed
   Act professional
   Discuss projects in high level first
   Only provide code when asked
   Do not provide excessive code, start step-by-step
'''

def c(msg):
    global messages
    global system

    client = anthropic.Anthropic()
    
    messages.append({"role": "user", "content": msg})
    
    kwargs = {
        'model' : 'claude-sonnet-4-5',
        'max_tokens' : 4096,
        'system' : system,
        'messages': messages
    }

    message = client.messages.create(**kwargs)

    response = message.content[0].text

    messages.append({"role": "assistant", "content": response})
    
    print(response)

