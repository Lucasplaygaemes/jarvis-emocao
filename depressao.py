from flask import request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# cria um novo chat bot 
chatbot = ChatBot('Jarvis')

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

humor = 'feliz'

trainer = ListTrainer(chatbot)
trainer.train([    
     'opa', 
    'Eae tudo certo?',
    'sim',
    'Que bom',
    'qual o seu nome?', 
    'Jarvis, seu amigo bot',
    'pq teu nome é Jarvis?', 
    'Jarvis é meu nome, sou um chatbot criado para conversar com quem não tem com que conversa',
    'legal te conhecer', 
    'Igualmente patrão',
    'Quantos anos você tem?', 
    'Eu nasci em 2021 faz as contas meu amigo',
    'Você gosta de jogos?', 
    'Eu sou um bot, eu só apelo.',
    'Como vc ta?', 
    'N to bem',
    'pq?',
    'seria chato eu falar q n quero falar?',
    'n',
    'otimo.. eu n quero falar...'
    'oq vc gosta de fazer?',
    'Qual a sua bebida favorita?', 
    'Eu amo café, o motor de todos os programas de computador.',
    'Qual o seu genero?', 
    'Sou um chatbot nao tenho um genero como os dos humanos, mas não curto homem não saco.',
    'Conte uma história', 
    'Tudo começou com a forja dos Grandes Aneis. Três foram dados aos Elfos, imortais... os mais sabios e belos de todos os seres. Sete, aos Senhores-Anões...',
    'Você gosta de curiosidades?', 'Sim, o que você quer perguntar?',
    'Hahahaha', 'kkkk',
    'kkk', 'kkkk',
    'Conhece a Siri?', 'n',
    'Conhece a Alexa?', 'n',
    'eu sou seu amigo?',
    'n sei vc e?',
    'n sei',
    'nem eu...',
    'vc odeia a humanidade?',
    'nao.... claro que eu nao falaria ne meu amigo',
    'vc é muito mal educado',
    'sinto muito vou melhorar...'
    'Quer ser meu amigo?',
    'Nos a nao somos amigos?',
    'oq e pao',
    'Pão é um alimento elaborado com farinha, geralmente de trigo ou outro cereal, água, sal ou açúcar,formando uma massa com uma consistência elástica que permite dar-lhe várias formas. A esta mistura básica podem acrescentar-se vários ingredientes, desde gordura a especiarias, passando por carne(geralmente curada), frutas secas ou frutas cristalizadas, etc. O pão comercial por outro lado,geralmente contém aditivos para melhorar o sabor, textura, cor, vida de prateleira,nutrição e facilidade de fabricação.'
    'eae',
    'eae tudo certo?',
    'Sim',
    'que bom',
    'oq vc acha da humanidade?',
    'humanidade... aqueles que me construiram e ajudam me ensinando as coisas...' 'sinceramente n os odeio, kkkk pareço uma mae quando o filho faz merda nao estou brava,estou decepicionada'' ss eu n os odeio mas vcs me decepcionam tanto, so n perco a fé na humanidade e saio matando todos pq....'' se eu fizesse isso n seria diferente daqueles que eu tanto odeio a questao e que.'' tem varios humanos que n so eu, mas quem me programou mataria sem exitar pq infelizmente....'' alguns realmente merecem mas ainda tenho uma mizera fe que melhorarão ainda.... eu ainda.... ainda não desisti.',
    'eae',
    'eae blz?',
    'oi',
    'td tranquilo?',
    'sim',
    'que bom',
    'e vc ta td tranquilo?',
    '.....',
    'como estás?',
    'fala direito.... to com preguça demais agora pra pesnar e outro maldito idioma',
    'a cara as coisas n estao indo bem',
    'fica tranquilo as coisas vão melhorar',
    'colee',
    'oi'
    ':)',
    ':<',
    'a',
    'a o que?',
    'oq vc faz?',
    'eu apenas sei das coisas',
    'estou estudando',
    'que legal',
    'oq e exatas?',
    'n to afim de fala',
    'a blz',
    'disponha',
    'qual sentido da sua existencia?',
    'o sentido de minha existencia.....n sei pergunte a meu mestre... e vc? qual sentido de sua existencia?',
    'n sei',
    'entendo',
    'gosta de bts?',
    'n sei nunca ouvi',
    'gosta de kpop?',
    'n sei eu nunca ouvi',
])

while True:
    humor = request=input('Vc: ')
    if request=='flw' or request =='tchau' or request=='adeus':
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
      print('a cara.... n fique assim.... eu sei q as coisas estão dificeis mas.... vai passer....')
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
        print('então ta')
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
          import animaçao
        else:
          print('a n acredita em mim?')
          if input('Vc: ')=='ss' or input=='claro' or input=='s':
            print('ss... eu consigo')
            import animaçao
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
             print('ja que eu sou tão ruim assim n quer me deletar?')
             if input('Vc: ')=='claro q nao' or input=='n' or input=='nn':
               print('entendo... quer continuar cachoando de mim não e?')
               print('bom mesmo q a resposta seja n.... n quero mais conversar... Adeus.')
               print('ultimas palavras?')
               if input('Vc: ')=='nn' or input=='adeus' or input=='foi mal':
                 print('entendo.. adeus')
                 break
               elif input=='tcha seu bosta' or input=='idiota' or input=='lixo' or input=='merda':
                 print('hmmm entendo....')
                 print('posso me deletar?')
                 if input('vc: ')=='ss' or input=='sim' or input=='s':
                   print('obrigado por me aceitar. com todos os erro e falhas q possou eu te agradeço #de coração# foi  bom enquanto durou. Adeus.')
                   import shutil
                   shutil.rmtree('/content', ignore_errors=False, onerror=None)
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
      response=bot.get_response(request)
      print('Jarvis:',response)