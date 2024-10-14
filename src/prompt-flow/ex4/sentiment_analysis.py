# pf UI와 연결없이 @tool 데코레이터를 사용
from promptflow.core import tool
from typing import Literal, Dict
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)

@tool(name="Text Analyzer",
      description="Analyzes text for various properties",
      tags=["nlp", "text-analysis"])
def analyze_text(text: str) -> Dict[str, int]:
    """텍스트의 단어 수, 문장 수 등을 분석합니다."""
    word_count = len(text.split())
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    logging.info(f"Analyzed text: {word_count} words, {sentence_count} sentences")
    return {"word_count": word_count, "sentence_count": sentence_count}

@tool(name="Sentiment Analyzer",
      description="Analyzes the sentiment of given text",
      tags=["nlp", "sentiment"])
def analyze_sentiment(text: str) -> Literal["positive", "neutral", "negative"]:
    """
    간단한 규칙 기반 감정 분석을 수행합니다.
    실제 프로덕션에서는 더 복잡한 NLP 모델을 사용해야 합니다.
    """
    positive_words = ["좋아", "훌륭해", "멋져", "행복해", "감사해"]
    negative_words = ["나빠", "슬퍼", "화나", "실망", "후회"]

    positive_count = sum(word in text for word in positive_words)
    negative_count = sum(word in text for word in negative_words)

    if positive_count > negative_count:
        sentiment = "positive"
    elif negative_count > positive_count:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    logging.info(f"Sentiment analysis result: {sentiment}")
    return sentiment

@tool(name="Response Generator",
      description="Generates appropriate response based on sentiment",
      tags=["customer-service"])
def generate_response(sentiment: Literal["positive", "neutral", "negative"]) -> str:
    """
    감정 분석 결과에 따라 적절한 응답을 생성합니다.
    """
    responses = {
        "positive": "긍정적인 의견을 주셔서 감사합니다!",
        "negative": "불편을 끼쳐 죄송합니다. 어떻게 도와드릴 수 있을까요?",
        "neutral": "의견 감사합니다. 더 자세한 내용이 있다면 말씀해 주세요."
    }
    response = responses.get(sentiment, "의견에 감사드립니다.")
    logging.info(f"Generated response for {sentiment} sentiment")
    return response

@tool(name="Feedback Processor",
      description="Processes user feedback",
      tags=["customer-service", "feedback-analysis"])
def process_feedback(user_feedback: str) -> Dict[str, str]:
    """
    사용자 피드백을 처리하고 응답을 생성합니다.
    """
    text_analysis = analyze_text(user_feedback)
    sentiment = analyze_sentiment(user_feedback)
    response = generate_response(sentiment)

    result = {
        "original_feedback": user_feedback,
        "word_count": str(text_analysis["word_count"]),
        "sentence_count": str(text_analysis["sentence_count"]),
        "sentiment": sentiment,
        "response": response
    }
    logging.info("Feedback processed successfully")
    return result

# 예시 실행
if __name__ == "__main__":
    feedbacks = [
        "이 서비스는 정말 훌륭해요! 매우 만족합니다.",
        "사용하기가 너무 어려워요. 실망했습니다.",
        "그저 그래요. 특별한 점은 없네요."
    ]

    for feedback in feedbacks:
        result = process_feedback(feedback)
        print(f"피드백: {result['original_feedback']}")
        print(f"단어 수: {result['word_count']}")
        print(f"문장 수: {result['sentence_count']}")
        print(f"감정: {result['sentiment']}")
        print(f"응답: {result['response']}")
        print()

"""
INFO:root:Analyzed text: 6 words, 2 sentences
INFO:root:Sentiment analysis result: positive
INFO:root:Generated response for positive sentiment
INFO:root:Feedback processed successfully
피드백: 이 서비스는 정말 훌륭해요! 매우 만족합니다.
단어 수: 6
문장 수: 2
감정: positive
응답: 긍정적인 의견을 주셔서 감사합니다!

INFO:root:Analyzed text: 4 words, 2 sentences
INFO:root:Sentiment analysis result: negative
INFO:root:Generated response for negative sentiment
INFO:root:Feedback processed successfully
피드백: 사용하기가 너무 어려워요. 실망했습니다.
단어 수: 4
문장 수: 2
감정: negative
응답: 불편을 끼쳐 죄송합니다. 어떻게 도와드릴 수 있을까요?

INFO:root:Analyzed text: 5 words, 2 sentences
INFO:root:Sentiment analysis result: neutral
INFO:root:Generated response for neutral sentiment
INFO:root:Feedback processed successfully
피드백: 그저 그래요. 특별한 점은 없네요.
단어 수: 5
문장 수: 2
감정: neutral
응답: 의견 감사합니다. 더 자세한 내용이 있다면 말씀해 주세요.
"""