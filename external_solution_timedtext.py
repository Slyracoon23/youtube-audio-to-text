from youtube_transcript_api import YouTubeTranscriptApi
from get_http_timed_text import timedtext_url

def get_timedtext(youtube_url):
    obj = timedtext_url(youtube_url)
    timedtext = YouTubeTranscriptApi.get_transcript(obj.get_videoid()[2:]) # get rid of fist two letters

    final_str = ' '.join(x['text'].replace('\n', ' ') for x in timedtext)

    return final_str


if __name__ == '__main__':
    obj = timedtext_url(input('type youtube url: '))
    timedtext = YouTubeTranscriptApi.get_transcript(obj.get_videoid()[2:]) # get rid of fist two letters

    final_str = ' '.join(x['text'].replace('\n', ' ') for x in timedtext)

    print(final_str)
