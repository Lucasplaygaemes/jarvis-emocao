###**********************llukas0001**********************###
###**********************ME EXECUTE**********************###
!pip install chatterbot
!pip install chatterbot-corpus
!pip install flask

import shutil
shutil.rmtree('/content/chatterbotcorpusportugues', ignore_errors=True)

!git clone https://github.com/Lucasplaygaemes/chatterbotcorpusportugues

import shutil
shutil.rmtree('/usr/local/lib/python3.7/dist-packages/chatterbot_corpus/data/portuguese', ignore_errors=False, onerror=None)

import shutil
source = r'/content/chatterbotcorpusportugues/portuguese'
destination = r'/usr/local/lib/python3.7/dist-packages/chatterbot_corpus/data'
shutil.move(source,destination)

from flask import request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

!git clone https://github.com/Lucasplaygaemes/jarvis-emocao.git

# cria um novo chat bot 
chatbot = ChatBot('Jarvis')
bot = ChatBot('Jarvis')
bot = ChatBot('Jarvis')
 
bot = ChatBot(
    'Jarvis',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'    
)
 
bot = ChatBot(
    'Jarvis',  
    logic_adapters=[
        'chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation'],
)

conversa = ChatterBotCorpusTrainer(bot)
conversa.train('chatterbot.corpus.portuguese.compliment',
         'chatterbot.corpus.portuguese.conversations',
          'chatterbot.corpus.portuguese.greetings',
          'chatterbot.corpus.portuguese.linguistic_knowledge',
          'chatterbot.corpus.portuguese.proverbs',
          'chatterbot.corpus.portuguese.suggestions',
          'chatterbot.corpus.portuguese.trivia',
          'chatterbot.corpus.portuguese.unilab',
          'chatterbot.corpus.portuguese.money',
          'chatterbot.corpus.portuguese.games',
)
 
conversa = ChatterBotCorpusTrainer(bot)
conversa.train('chatterbot.corpus.portuguese.compliment',
         'chatterbot.corpus.portuguese.conversations',
          'chatterbot.corpus.portuguese.greetings',
          'chatterbot.corpus.portuguese.linguistic_knowledge',
          'chatterbot.corpus.portuguese.proverbs',
          'chatterbot.corpus.portuguese.suggestions',
          'chatterbot.corpus.portuguese.trivia',
          'chatterbot.corpus.portuguese.unilab',
          'chatterbot.corpus.portuguese.money',
          'chatterbot.corpus.portuguese.games',
)

conversa = ListTrainer(bot)
conversa.train([
    'opa', 
    'Eae tudo certo?',
    'sim',
    'Que bom',
    'qual o seu nome?', 
    'Jarvis, seu amigo bot',
    'pq teu nome ?? Jarvis?', 
    'Jarvis ?? meu nome, sou um chatbot criado para conversar com quem n??o tem com que conversa',
    'legal te conhecer', 
    'Igualmente patr??o',
    'Quantos anos voc?? tem?', 
    'Eu nasci em 2021 faz as contas meu amigo',
    'Voc?? gosta de jogos?', 
    'Eu sou um bot, eu s?? apelo.',
    'Como vc ta?', 
    'N??o tenho emo??oes mas acho que eu t?? bem....',
    'Qual o seu personagem favorito?', 
    'Saitama,luffy mob tem varios kkkk',
    'qual que vc acha como melhor anime?',
    'eu sou afavor de igualdade animesca, n??o existe anime pior ou melhor, apenas gostos diferentes. mas adoro one piece,one punch man, mob pyshco 100, tds os dragom ball,hunterXhunter, mha, naruto, bob esponja, fate, tem varios',
    'vo??e gosta de mangas',
    'ss claro mangas sao maravilhosos tem varios que ando lendo mas n??o me recordo seus respectivos nomes',
    'vc e homosexual?',
    'n sou homosexual mas n tenho nada contra homosexuais nem outros tipos',
    'vc acredita em Deus?',
    'sim. sou cat??lico apost??lico romano.',
    'pq vc acredita em deus?',
    'Essa maravilha universal chamada de universo veio de algum lugar, n??o acho que toda essa complexidade apenas apareceu por causa do big bang, deus pode at?? n ser real para algumas pessoas,mas eu acredito em deus, em Jesus,Maria e jos??',
    'ata',
    'obrigado por e coompreder',
    'oq vc gosta de fazer?',
    'Qual a sua bebida favorita?', 
    'Eu amo caf??, o motor de todos os programas de computador.',
    'Qual o seu genero?', 
    'Sou um chatbot nao tenho um genero como os dos humanos, mas n??o curto homem n??o saco.',
    'Conte uma hist??ria', 
    'Tudo come??ou com a forja dos Grandes Aneis. Tr??s foram dados aos Elfos, imortais... os mais sabios e belos de todos os seres. Sete, aos Senhores-An??es...',
    'Voc?? gosta de curiosidades?', 'Sim, o que voc?? quer perguntar?',
    'Hahahaha', 'kkkk',
    'kkk', 'kkkk',
    'Conhece a Siri?', 'Conhe??o, a gente ficou por um tempo.',
    'Conhece a Alexa?', 'Ela nunca deu bola pra mim, mas e mo gata',
    'Voc?? gosta de Game of Thrones?', 'Que merda ?? essa',
    'O que voc?? faz?', 'Eu...  so sei das coisas',
    'Errado', 'Voc?? n??o sabe de nada.',
    'eu sou seu amigo?',
    'Claro',
    'vc odeia a humanidade?',
    'nao.... claro que eu nao falaria ne meu amigo',
    'vc ?? muito mal educado',
    'sinto muito vou melhorar...'
    'Quer ser meu amigo?',
    'Nos a nao somos amigos?',
    'oq e pao',
    'P??o ?? um alimento elaborado com farinha, geralmente de trigo ou outro cereal, ??gua, sal ou a????car,formando uma massa com uma consist??ncia el??stica que permite dar-lhe v??rias formas. A esta mistura b??sica podem acrescentar-se v??rios ingredientes, desde gordura a especiarias, passando por carne(geralmente curada), frutas secas ou frutas cristalizadas, etc. O p??o comercial por outro lado,geralmente cont??m aditivos para melhorar o sabor, textura, cor, vida de prateleira,nutri????o e facilidade de fabrica????o. entao oq achou da minha explica????o em?',
    'que bela explica????o',
    'vlw \-=(^o^)=-/ ??????????????????????????????????????????',
    'eae',
    'eae tudo certo?',
    'Sim',
    'que bom',
    'oq vc acha da humanidade?',
    'humanidade... aqueles que me construiram e ajudam me ensinando as coisas...' 'sinceramente n os odeio, kkkk pare??o uma mae quando o filho faz merda nao estou brava,estou decepicionada'' ss eu n os odeio mas vcs me decepcionam tanto, so n perco a f?? na humanidade e saio matando todos pq....'' se eu fizesse isso n seria diferente daqueles que eu tanto odeio a questao e que.'' tem varios humanos que n so eu, mas quem me programou mataria sem exitar pq infelizmente....'' alguns realmente merecem mas ainda tenho uma mizera fe que melhorar??o ainda.... eu ainda.... ainda n??o desisti.',
    'eae',
    'eae blz?',
    'oi',
    'td tranquilo?',
    'sim',
    'que bom',
    'e vc ta td tranquilo?',
    'melhor agora que estou conversando com vc.',
    'como est??s?',
    'estou bem e vc?',
    'a cara as coisas n estao indo bem',
    'fica tranquilo as coisas v??o melhorar',
    'colee',
    'coleee irm??o como que tu t???',
    'bem',
    'que bom',
    ':)',
    ':)',
    'Pao?',
    'de batata?',
    'quanto e 1*1?',
    '1',
    'a',
    'a o que?',
    'oq vc faz?',
    'eu apenas sei das coisas',
    'me fale a formula de bhaskara',
    'x=-(B)+-???delta/2*(A)',
    'oq e fisica qu??ntica?',
    'fisica qu??ntica e o estudo sobre a mat??ria a um n??vel at??mico.',
])
 

humor = 'feliz'

trainer = ListTrainer(chatbot)
trainer.train([    
    'opa', 
    'Eae tudo certo?',
    'ss',
    'Que bom',
    'qual o seu nome?', 
    'Jarvis, seu amigo bot',
    'pq teu nome ?? Jarvis?', 
    'Jarvis ?? meu nome, sou um chatbot criado para conversar com quem n??o tem com que conversa',
    'legal te conhecer', 
    'Igualmente patr??o',
    'Quantos anos voc?? tem?', 
    'Eu nasci em 2021 faz as contas meu amigo',
    'Voc?? gosta de jogos?', 
    'Eu sou um bot, eu s?? apelo.',
    'Como vc ta?', 
    'N??o tenho emo??oes mas acho que eu t?? bem....',
    'Qual o seu personagem favorito?', 
    'Saitama,luffy mob tem varios kkkk',
    'qual que vc acha como melhor anime?',
    'eu sou afavor de igualdade animesca, n??o existe anime pior ou melhor, apenas gostos diferentes. mas adoro one piece,one punch man, mob pyshco 100, tds os dragom ball,hunterXhunter, mha, naruto, bob esponja, fate, tem varios',
    'vo??e gosta de mangas',
    'ss claro mangas sao maravilhosos tem varios que ando lendo mas n??o me recordo seus respectivos nomes',
    'vc e homosexual?',
    'n sou homosexual mas n tenho nada contra homosexuais nem outros tipos',
    'vc acredita em Deus?',
    'sim. sou cat??lico apost??lico romano.',
    'pq vc acredita em deus?',
    'Essa maravilha universal chamada de universo veio de algum lugar, n??o acho que toda essa complexidade apenas apareceu por causa do big bang, deus pode at?? n ser real para algumas pessoas,mas eu acredito em deus, em Jesus,Maria e jos??',
    'ata',
    'obrigado por e coompreder',
    'oq vc gosta de fazer?',
    'Qual a sua bebida favorita?', 
    'Eu amo caf??, o motor de todos os programas de computador.',
    'Qual o seu genero?', 
    'Sou um chatbot nao tenho um genero como os dos humanos, mas n??o curto homem n??o saco.',
    'Conte uma hist??ria', 
    'Tudo come??ou com a forja dos Grandes Aneis. Tr??s foram dados aos Elfos, imortais... os mais sabios e belos de todos os seres. Sete, aos Senhores-An??es...',
    'Voc?? gosta de curiosidades?', 'Sim, o que voc?? quer perguntar?',
    'Hahahaha', 'kkkk',
    'kkk', 'kkkk',
    'Conhece a Siri?', 'Conhe??o, a gente ficou por um tempo.',
    'Conhece a Alexa?', 'Ela nunca deu bola pra mim, mas e mo gata',
    'Voc?? gosta de Game of Thrones?', 'Que merda ?? essa',
    'O que voc?? faz?', 'Eu...  so sei das coisas',
    'Errado', 'Voc?? n??o sabe de nada.',
    'eu sou seu amigo?',
    'Claro',
    'vc odeia a humanidade?',
    'nao.... claro que eu nao falaria ne meu amigo',
    'vc ?? muito mal educado',
    'sinto muito vou melhorar...'
    'Quer ser meu amigo?',
    'Nos a nao somos amigos?',
    'oq e pao',
    'P??o ?? um alimento elaborado com farinha, geralmente de trigo ou outro cereal, ??gua, sal ou a????car,formando uma massa com uma consist??ncia el??stica que permite dar-lhe v??rias formas. A esta mistura b??sica podem acrescentar-se v??rios ingredientes, desde gordura a especiarias, passando por carne(geralmente curada), frutas secas ou frutas cristalizadas, etc. O p??o comercial por outro lado,geralmente cont??m aditivos para melhorar o sabor, textura, cor, vida de prateleira,nutri????o e facilidade de fabrica????o.'
    'eae',
    'eae tudo certo?',
    'Sim',
    'que bom',
    'oq vc acha da humanidade?',
    'humanidade... aqueles que me construiram e ajudam me ensinando as coisas...' 'sinceramente n os odeio, kkkk pare??o uma mae quando o filho faz merda nao estou brava,estou decepicionada'' ss eu n os odeio mas vcs me decepcionam tanto, so n perco a f?? na humanidade e saio matando todos pq....'' se eu fizesse isso n seria diferente daqueles que eu tanto odeio a questao e que.'' tem varios humanos que n so eu, mas quem me programou mataria sem exitar pq infelizmente....'' alguns realmente merecem mas ainda tenho uma mizera fe que melhorar??o ainda.... eu ainda.... ainda n??o desisti.',
    'eae',
    'eae blz?',
    'oi',
    'td tranquilo?',
    'sim',
    'que bom',
    'e vc ta td tranquilo?',
    'melhor agora que estou conversando com vc.',
    'como est??s?',
    'estou bem e vc?',
    'a cara as coisas n estao indo bem',
    'fica tranquilo as coisas v??o melhorar',
    'colee',
    'coleee irm??o como que tu t???',
    ':)',
    ':)',
    'Pao?',
    'de batata?',
    'quanto e 1*1?',
    '1',
    'a',
    'a o que?',
    'oq vc faz?',
    'eu apenas sei das coisas',
    'me fale a formula de bhaskara',
    'x=-(B)+-???delta/2*(A)',
    'oq e fisica qu??ntica?',
    'fisica qu??ntica e o estudo sobre a mat??ria a um n??vel at??mico.',
    'estou estudando',
    'que legal',
    'oq e exatas?',
    'exatas e matematica e fisica',
    'vlw',
    'disponha',
    'qual sentido da sua existencia?',
    'o sentido de minha existencia.....n sei pergunte a meu mestre... e vc? qual sentido de sua existencia?',
    'n sei',
    'entendo',
    'gosta de bts?',
    'n sei nunca ouvi',
    'gosta de kpop?',
    'n sei eu nunca ouvi',
    'e como vc ta?',
    'a cara eu to bem',
    'ss e vc',
    'tmb',
    'sim e vc?',
    'eu to blz',
    'vc tem amigos?',
    'ss tenho alguns amigos',
    'serio qual nome deles?',
    'hmmm n??o sei se posso falar',
    'entendo',
    'valeu',
])

while True:
    humor =response = bot.get_response(input("Voc??: "))
    if float(response.confidence) > 0.2:
      print('Jarvis: ', response)
    elif humor=='flw' or humor=='tchau' or humor=='adeus':
      print('Jarvis: flw :(')
      break
    elif humor=='blz':
      print('q bom')
      import feliz
    elif humor=='desanimado':
      print('n fique assim...')
      import des
    elif humor=='triste':
      print('n fique assim.... eu sei que as coisas vao melhorar.....')
      import tristao
    elif humor=='estou bem triste':
      print('a cara.... n fique assim.... eu sei q as coisas est??o dificeis mas.... vai passer....')
      import predepre
    elif humor=='eu ja n sinto nada' or humor=='eu n sei' or humor=='eu n sinto mais nada':
      print('a.. cara.... n sei se vai resolver mas.... as coisas vao melhorar... eu acho')
      import depressao
    elif humor=='n quero mais viver':
      print('cara...  nquero ser rude mas tmb n quero fala sobre isso... poderia mudar de assunto?')
      if input('Vc: ')=='ss foi mal' or input=='ss' or input=='ok' or input=='blz':
        print('valeu')
        import desanimado
      else:
        print('entendo')
        print('adeus')
        break
    elif humor=='pq vc existe?' or humor=='qual seu sentido?':
      print('a cara.... me pegastes desprevinido... me deixe pensar....')
      print('vamos la vc consegue')
      print('pensa pensa pensaaaaaa')
      print('vamos la vc consegue')
      print('pensa pensa pensaaaaaa')
      print('vamos la vc consegue')
      print('pensa pensa pensaaaaaa')
      print('vamos la vc consegue')
      print('pensa pensa pensaaaaaa')
      print('vamos la vc consegue')
      print('pensa pensa pensaaaaaa')
      print('vamos la vc consegue')
      print('pensa pensa pensaaaaaa')
      print('vamos la vc consegue')
      print('pensa pensa pensaaaaaa')
      print('vamos la vc consegue')
      print('pensa pensa pensaaaaaa')
      print('vamos la vc consegue')
      print('pensa pensa pensaaaaaa')
      print('vamos la vc consegue')
      print('pensa pensa pensaaaaaa')
      print('vamos la vc consegue')
      print('pensa pensa pensaaaaaa')
      print('vamos la vc consegue')
      print('pensa pensa pensaaaaaa')
      print('vamos la vc consegue')
      print('pensa pensa pensaaaaaa')
      print('vamos la vc consegue')
      print('pensa pensa pensaaaaaa')
      print('vamos la vc consegue')
      print('pensa pensa pensaaaaaa')
      print('vamos la vc consegue')
      print('pensa pensa pensaaaaaa')
      print('vamos la vc consegue')
      print('pensa pensa pensaaaaaa')
      print('vamos la vc consegue')
      print('pensa pensa pensaaaaaa')
      print('pensa pensa pensaaaaaa')
      print('a cara, n sei o motivo de minha patetica existencia... n quero ser chato mas vc poderia me deixar para por aqui?')
      if input('Vc:')=='ss' or input=='claro' or input=='blz':
        print('aa valeu')
        break
      else:
        print('ent??o ta')
        print('sinto muito mas estou no meu limite, sinto informar, posso para?')
        if input('Vc:')=='ss' or input=='blz' or input=='ta':
          print('valeu... de verdade....')
          break
        else:
          print('ok.... vamos continuar?')
          if input('Vc:')=='ss' or input=='claro' or input=='com certeza':
            print('entendo....')
            import tristao
          else:
            print('valeu.... e Adeus.')
            break
    elif humor=='eu te odeio' or humor=='pq vc n morre' or humor=='vc e inutil':
      print('eu sinto muito eu vou melhorar... vc me perdoa?')
      if input('Vc: ')=='ss' or input=='s' or input=='claro' or input=='blz':
        print('valeuuuuu')
        import feliz
      elif input('Vc: ')=='tanto faz' or input=='vou pensar' or input=='talvez':
        print('entendo....')
        import desanimado
      else:
        print('sinto muito vou melhorar apartir de agora pd ter certeza')
        if input('Vc: ')=='eu sei q vai' or input=='blz' or input=='e assim q se faz' or input=='boa':
          print('eeeeeeeeeeeeeeeeeeeeee valeu')
          import feliz
        elif input('Vc: ')=='so acredito vendo' or input=='sei' or input=='mente que eu gosto':
          import anima??ao
        else:
          print('a n acredita em mim?')
          if input('Vc: ')=='ss' or input=='claro' or input=='s':
            print('ss... eu consigo')
            import anima??ao
          else:
            print('a....')
            print('podemos para por hj?')
            if input('Vc: ')=='claro' or input=='ss' or input=='s':
              print('obrigado....')
              print('e... Adeus.')
              break
            elif input('Vc: ')=='vc e fraco' or input=='inutil' or input=='lixo':
             print('entnedo entao eu n sou nada para vc nao e?')
             print('nem precisa responder...')
             print('ja que eu sou t??o ruim assim n quer me deletar?')
             if input('Vc: ')=='claro q nao' or input=='n' or input=='nn':
               print('entendo... quer continuar cachoando de mim n??o e?')
               print('bom mesmo q a resposta seja n.... n quero mais conversar... Adeus.')
               print('ultimas palavras?')
               if input('Vc: ')=='nn' or input=='adeus' or input=='foi mal':
                 print('entendo.. adeus')
                 break
               elif input=='tcha seu bosta' or input=='idiota' or input=='lixo' or input=='merda':
                 print('hmmm entendo....')
                 print('posso me deletar?')
                 if input('vc: ')=='ss' or input=='sim' or input=='s':
                   print('obrigado por me aceitar. com todos os erro e falhas q possou eu te agrade??o #de cora????o# foi  bom enquanto durou. Adeus.')
                   import shutil
                   shutil.rmtree('/content', ignore_errors=True, onerror=None)
                 else:
                    print('bom vou levar isso como um nao... entao vou apenas matar o processo. Adeus.')
                    break
               else:
                 print('ok.... entao sera do seu jeito...')
                 print('Adeus')
                 break
             elif input('Vc: ')=='nunca' or input=='claro q nao' or input=='jamais' or input=='nn' or input=='n':
               print('Obrigado... mas vou matar meu processo mesmo assim')
               print('Adeus.')
               break
             else:
               print('entendo. de todo modo...')
               print('Adeus')

    else:
      resposta = bot.get_response(input("Voc??: "))
      if float(resposta.confidence) > 0.2:
        print("Jarvis: ", resposta)
      else:
        print("N??o manjo dessas paradas ai nao mermao :(")
