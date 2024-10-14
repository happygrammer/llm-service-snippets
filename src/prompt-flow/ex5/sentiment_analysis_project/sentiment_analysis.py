from typing import Dict, Literal
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)

def analyze_text(text: str) -> Dict[str, int]:
    """텍스트의 단어 수, 문장 수 등을 분석합니다."""
    word_count = len(text.split())
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    logging.info(f"Analyzed text: {word_count} words, {sentence_count} sentences")
    return {"word_count": word_count, "sentence_count": sentence_count}

def analyze_sentiment(text: str) -> Literal["positive", "neutral", "negative"]:
    """간단한 규칙 기반 감정 분석을 수행합니다."""
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

def generate_response(sentiment: Literal["positive", "neutral", "negative"]) -> str:
    """감정 분석 결과에 따라 적절한 응답을 생성합니다."""
    responses = {
        "positive": "긍정적인 의견을 주셔서 감사합니다!",
        "negative": "불편을 끼쳐 죄송합니다. 어떻게 도와드릴 수 있을까요?",
        "neutral": "의견 감사합니다. 더 자세한 내용이 있다면 말씀해 주세요."
    }
    response = responses.get(sentiment, "의견에 감사드립니다.")
    logging.info(f"Generated response for {sentiment} sentiment")
    return response

from promptflow import tool

# @tool은 하나의 함수에만 적용할 수 있음
@tool
def process_feedback(user_feedback: str) -> Dict[str, str]:
    """사용자 피드백을 처리하고 응답을 생성합니다."""
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

# 예시 실행 (이 부분은 실제 Prompt Flow 실행 시에는 필요 없음)
if __name__ == "__main__":
    feedback = "이 서비스는 정말 훌륭해요! 매우 만족합니다."
    result = process_feedback(feedback)
    print(result)