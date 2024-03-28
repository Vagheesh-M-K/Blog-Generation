from langchain.prompts import PromptTemplate
template= "Write an engaging, interesting blog in about {n_words} on the topic {topic}\
      for {target_audience}.Reherse\re-study\re-visit the initially created content if any modification\
        is deemed appropriate"
prompt_template = PromptTemplate(template = template, input_variables =
                                  ['n_words', 'topic', 'target_audience'])



