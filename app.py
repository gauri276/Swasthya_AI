from gtts import gTTS

text = """
Hello everyone!
We are Team Binary_Hum, and we’re excited to present our solution — SwasthyaAI.

SwasthyaAI is a smart healthcare assistant designed to support rural communities and frontline health workers.
It comes packed with 9 powerful features, including offline-first access and support for 4+ regional languages, making healthcare more inclusive and accessible.

One of our key tools is the Pregnancy Risk Assessment feature.
It collects vital information such as age, previous pregnancies, and symptoms — and uses AI to classify the risk as low, moderate, or high — helping new mothers receive the right care at the right time.

We’ve also added a Local Dietary Suggestion feature, tailored by region — North, South, East, West — and based on vegetarian or non-vegetarian preferences, respecting local food culture.

Our Health Scheme Finder recommends relevant state and central government schemes based on income, pregnancy stage, and age — and simplifies the application process.

With an in-app Voice Assistant, health history tracker, and a doctor-view mode for quick access to patient data —
SwasthyaAI empowers healthcare, one village at a time.
"""

tts = gTTS(text=text, lang='en', tld='co.in')
tts.save("swasthya_ai_voiceover.mp3")
print("Voiceover saved as swasthya_ai_voiceover.mp3")
