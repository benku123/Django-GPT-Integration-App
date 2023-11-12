# views.py
from openai import OpenAI
from django.shortcuts import render
from .forms import GPTForm


def gpt_view(request):
    llm = OpenAI(api_key="your_api_key")
    response_text = ""
    if request.method == 'POST':
        form = GPTForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['user_input']
            completion = llm.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=[
                    {"role": "user", "content": input_text},
                ]
            )

            response_text = completion.choices[0].message.content
            print(response_text)


    else:
        form = GPTForm()

    return render(request, 'gpt_form.html', {'form': form, "response": response_text})
