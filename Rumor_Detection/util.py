import stanza
import re
from urduhack.normalization import normalize
from urduhack.stop_words import STOP_WORDS
from googletrans import Translator
from langdetect import detect
from langdetect import LangDetectException
import joblib
import sklearn

MODEL = None



def manual_tokenize(tweet):
    tokens = re.findall(r'\b\w+\b', tweet)
    return tokens


def remove_links_and_emails(tweet):
    tweet = re.sub(r'https?://\S+', ' ', tweet)
    tweet = re.sub(r'\S+@\S+', ' ', tweet)
    return tweet


def preprocessing_tweet(tweet):
    tweet = normalize(tweet)
    tweet = remove_links_and_emails(tweet)
    tweet = manual_tokenize(tweet)
    tweet = [word for word in tweet if word not in STOP_WORDS]
    return tweet


def translate_to_urdu(tweet):
    tweet = remove_links_and_emails(tweet)
    translator = Translator()
    translated = translator.translate(tweet, src='en', dest='ur')
    return translated.text


def preprocessing_all_tweets(tweet):
    if not isinstance(tweet, str) or not tweet.strip():
        return ""
    preprocessed_tweet = remove_links_and_emails(tweet)
    if not preprocessed_tweet.strip():
        return ""

    try:
        language = detect(preprocessed_tweet)
    except LangDetectException:
        print(f"Could not detect language for: {tweet}")
        language = "unknown"

    if language == "ur":
        return preprocessing_tweet(tweet)
    elif language == "en":
        return preprocessing_tweet(translate_to_urdu(tweet))
    else:
        print("Not Supported")


def lematizing_the_tweet(tweet):
    if tweet is None:
        return None

    tweet = " ".join(tweet)
    stanza.download("ur")
    nlp = stanza.Pipeline("ur", processors="tokenize, lemma")
    doc = nlp(tweet)
    lemmatized_tweet = " ".join([word.lemma for sent in doc.sentences for word in sent.words])
    return lemmatized_tweet


def model_loading():
    global MODEL
    try:
        print("Attempting to load the model...")
        MODEL = joblib.load("decision_tree_classifier_model_lemmatized_scaled.joblib")
        print("Model loaded successfully!")
    except Exception as e:
        print(f"An error occurred while loading the model: {e}")
    return MODEL


def customization(tweet, views, bookmark_count, favorite_count, quote_count, reply_count, retweet_count):
    tweet = preprocessing_all_tweets(tweet)
    tweet = lematizing_the_tweet(tweet)
    result = MODEL.predict([[tweet, views, bookmark_count, favorite_count, quote_count, reply_count, retweet_count]])
    return result


if __name__ == "__main__":
    print("CSK")
    # tweets = [
    #     "یہ آج کا موسم بہت خوبصورت ہے! 🌞 https://weather.com",
    #     "Aaj ka mausam bohot acha hai! 🌞 https://weather.com",
    #     "Just saw a great movie! 🎬 Check it out at https://moviereviews.com",
    #     "The event was amazing! واقعی بہترین تھا. 📅",
    #     "Kal meeting hai, mujhe zaroor jana chahiye. 📧 example@example.com https://meetinglink.com",
    #     "https://moviereviews.com"
    # ]
    # new_list = [preprocessing_all_tweets(tweet) for tweet in tweets]
    # print(new_list)
    # new_list_filtered = [tweet for tweet in new_list if tweet is not None]
    # new_list_1 = [lematizing_the_tweet(tweet) for tweet in new_list_filtered]
    # print(new_list_1)
    model_loading()
    # new_result = customization("""
    # دعویٰ: پنجاب کی وزیر اطلاعات نے دعویٰ کیا ہے کہ پاکستان میں سوشل میڈیا پلیٹ فارم بغیر سرکاری رولز کے کام کر رہے ہیں۔
    #
    # """, 805, 1, 8, 1, 0, 7)  # False
    new_result = customization("""Not many knew about the virtual jalsa until they shut the internet. Now the whole world knows about this jalsa. The kind of brains we have in Pakistan. 😂

    #PTIVirtualJalsa""", 111181, 19, 867335, 35, 148, 1760)  # True
    print("CSK")
    print(new_result[0])
