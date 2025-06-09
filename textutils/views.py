from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get input text and checkbox values
    djtext = request.POST.get('text', '')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    analyzed = djtext
    purpose = []

    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = "".join(char for char in analyzed if char not in punctuations)
        purpose.append("Removed Punctuation")

    if fullcaps == "on":
        analyzed = analyzed.upper()
        purpose.append("Converted to UPPERCASE")

    if newlineremover == "on":
        analyzed = "".join(char for char in analyzed if char != '\n' and char != '\r')
        purpose.append("Removed New Lines")

    if extraspaceremover == "on":
        analyzed = " ".join(analyzed.split())
        purpose.append("Removed Extra Spaces")

    if charcount == "on":
        count = len(analyzed)
        analyzed += f"\n\nTotal Characters: {count}"
        purpose.append("Character Count")

    if not purpose:
        return render(request, 'analyze.html', {
            'purpose': 'No operation selected',
            'analyzed_text': 'Please select at least one option and try again.'
        })

    return render(request, 'analyze.html', {
        'purpose': ', '.join(purpose),
        'analyzed_text': analyzed
    })
