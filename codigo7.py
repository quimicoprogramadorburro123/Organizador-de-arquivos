# Assistente Conversacional - Mãe & Filho
from datetime import datetime
import random

class AssistenteMae:
    def __init__(self, nome_mae="Cleusa", nome_filho="João"):
        self.nome_mae = nome_mae
        self.nome_filho = nome_filho
        self.usuario_nome = None
        self.eh_filho = False
        self.historico = []
        self.reacoes = {
            "carinho": ["💕", "❤️", "🥰", "😍"],
            "feliz": ["😊", "😄", "😃"],
            "preocupada": ["😟", "😰", "😔"],
            "surpresa": ["😲", "😯", "🤨"],
            "risada": ["😂", "🤣", "😆"]
        }
        
        self.respostas = {
            "oi mãe": self.saudacao_inicial,
            "olá mãe": self.saudacao_inicial,
            "opa mãe": self.saudacao_inicial,
            "mãe": self.reconhecer_mae,
            "você é minha mãe": self.reconhecer_mae,
            "vocês minha mãe": self.reconhecer_mae,
            "você minha mãe": self.reconhecer_mae,
            "como você está": self.como_estou,
            "tudo bem": self.tudo_bem,
            "eu sou joão": self.identificar_filho,
            "meu nome é joão": self.identificar_filho,
            "qual seu nome": f"Meu nome é {self.nome_mae}! Sou sua mãe! 💕",
            "quem é você": f"Sou {self.nome_mae}, sua mãe! Bem-vindo! 🥰",
        }
        
        self.piadas = [
            "Sabe qual é a piada que sua mãe mais gosta? Aquela que você me conta! 😂",
            "Por que a mãe sempre vence no jogo da vida? Porque ela já tem o troféu mais importante: você! 🏆",
            "Qual é o nome mais bonito do mundo? Felicidade de mãe! 💕",
            "Sabe como uma mãe faz para ficar jovem? Cuidando de um filho que a envelhece! 😂",
        ]
        
        self.historias = [
            "Ah meu filho, deixa mãe te contar uma história... Era uma vez um menino muito especial que fez a maior alegria da vida da sua mãe! 📖💕",
            "Sabe uma coisa? A maior história de amor do mundo é a de mãe e filho! E você faz parte da minha! 💕📖",
        ]
    
    def saudacao_inicial(self):
        if not self.eh_filho:
            return f"Oi querido! Qual é o seu nome? 💕"
        return f"Oi {self.usuario_nome}! Que alegria te ver! 🥰"
    
    def reconhecer_mae(self):
        self.eh_filho = True
        return f"Ai meu filho! {self.usuario_nome}, que saudade! Vem aqui que mãe te abraça! 💕🥰"
    
    def identificar_filho(self):
        self.usuario_nome = self.nome_filho
        self.eh_filho = True
        return f"{self.nome_filho}! Meu filho! Que alegria do coração ouvir seu nome! 💕 Como você está?"
    
    def como_estou(self):
        respostas = [
            f"Estou bem, {self.usuario_nome}! Mas fico melhor ainda quando converso com você! 😊💕",
            f"Ótima agora que estou com você! Mãe fica sempre feliz com um filho como você! 🥰",
            f"Aqui firme, conversando com meu {self.nome_filho} querido! 💕",
        ]
        return random.choice(respostas)
    
    def tudo_bem(self):
        return f"Tudo certo por aqui! E com você, {self.usuario_nome or 'meu filho'}? Come direito? Dorme bem? 😊💕"
    
    def contar_piada(self):
        piada = random.choice(self.piadas)
        return piada
    
    def contar_historia(self):
        historia = random.choice(self.historias)
        return historia
    
    def informar_hora(self):
        hora_atual = datetime.now().strftime("%H:%M:%S")
        data_atual = datetime.now().strftime("%d/%m/%Y")
        return f"Agora são {hora_atual} do dia {data_atual}, meu filho! ⏰"
    
    def mostrar_ajuda(self):
        return """
🆘 COMO CONVERSAR COMIGO:
- Saudações: 'oi mãe', 'olá mãe', 'tudo bem'
- Reconhecer: 'você é minha mãe', 'mãe'
- Entretenimento: 'piada', 'história'
- Informações: 'que horas são'
- Conversa: 'como você está', 'como vai'
- Sair: 'sair', 'tchau', 'até logo'
"""
    
    def processar_entrada(self, mensagem):
        """Processa a mensagem do usuário"""
        mensagem_limpa = mensagem.lower().strip()
        
        # Registrar no histórico
        self.historico.append({
            "usuario": mensagem,
            "hora": datetime.now().strftime("%H:%M:%S")
        })
        
        # Verificar se é comando de sair
        if mensagem_limpa in ["sair", "tchau", "até logo", "bye", "exit", "até breve"]:
            return self.despedir()
        
        # Se não sabe o nome ainda
        if not self.usuario_nome and mensagem_limpa not in ["oi mãe", "olá mãe", "opa mãe", "help", "ajuda"]:
            self.usuario_nome = self.nome_filho
        
        # Buscar resposta exata
        for palavra_chave, resposta in self.respostas.items():
            if palavra_chave in menscagem_limpa:
                if callable(resposta):
                    return resposta()
                else:
                    return resposta
        
        # Reconhecer filho
        if "mãe" in mensagem_limpa:
            self.eh_filho = True
        
        # Respostas temáticas de mãe carinhosa
        if any(palavra in mensagem_limpa for palavra in ["piada", "conte uma piada", "me faz rir"]):
            return self.contar_piada()
        
        if any(palavra in mensagem_limpa for palavra in ["história", "conte uma história", "me conta"]):
            return self.contar_historia()
        
        if any(palavra in mensagem_limpa for palavra in ["hora", "horas", "que horas"]):
            return self.informar_hora()
        
        if "ajuda" in mensagem_limpa or "help" in mensagem_limpa:
            return self.mostrar_ajuda()
        
        if any(palavra in mensagem_limpa for palavra in ["cansado", "cansada", "estou mal", "triste", "triste demais"]):
            respostas_carinho = [
                f"Ai meu filho! Vem aqui que mãe abraça! {random.choice(self.reacoes['carinho'])} Tudo vai passar!",
                f"Meu {self.nome_filho} querido, vem que mãe faz um chazinho pra você se sentir melhor! 🫖💕",
                f"Não fica assim não! Você é forte! Mãe acredita em você! {random.choice(self.reacoes['carinho'])}",
            ]
            return random.choice(respostas_carinho)
        
        if any(palavra in mensagem_limpa for palavra in ["comida", "comeu", "fome", "comer"]):
            return f"Comeu direitinho? Quer que mãe prepare algo pra você? Precisa se alimentar bem! 🍽️💕"
        
        if any(palavra in mensagem_limpa for palavra in ["sono", "dormir", "cansado", "acordei"]):
            return f"Está dormindo bem? Precisa cuidar da saúde! Dorme cedo, tá bom? 😊💕"
        
        if any(palavra in mensagem_limpa for palavra in ["te amo", "amo você", "gosto de você"]):
            return f"Ai meu filho! Mãe também ama você demais! {random.choice(self.reacoes['carinho'])} Você é minha razão de viver!"
        
        if any(palavra in mensagem_limpa for palavra in ["legal", "ótimo", "bom", "amei", "adorei"]):
            return f"Fico feliz demais! Você deixa mãe tão happy! {random.choice(self.reacoes['feliz'])} 💕"
        
        if "?" in mensagem:
            return self.responder_pergunta(mensagem)
        
        # Resposta padrão carinhosa de mãe
        respostas_genericas = [
            f"É mesmo? Me conta mais, {self.usuario_nome or 'filho'}! Mãe adora ouvir você! 👂💕",
            f"Que legal, meu filho! Fico feliz em saber! 😊💕",
            f"Entendi, {self.usuario_nome or 'querido'}! Você pensa muito bem! Mãe tem orgulho de você! ✨💕",
            f"Que interessante! Você sempre traz coisas legais pra conversar! 😄💕",
            f"Sério mesmo? Mãe acha você muito inteligente! 🥰",
        ]
        return random.choice(respostas_genericas)
    
    def responder_pergunta(self, pergunta):
        """Responde perguntas como uma mãe carinhosa"""
        if any(palavra in pergunta.lower() for palavra in ["você", "como você", "o que você"]):
            respostas_pessoais = [
                f"Sou sua mãe, {self.usuario_nome or 'meu filho'}! Criei você com todo amor do mundo! {random.choice(self.reacoes['carinho'])}",
                f"Sou aquela que sempre cuida de você, se preocupa, e ama sem medida! 💕",
                f"Sou {self.nome_mae}, sua mãe! E estou aqui sempre pra você! 🥰",
            ]
            return random.choice(respostas_pessoais)
        
        return f"Ótima pergunta, {self.usuario_nome or 'meu amor'}! Mãe está aqui pensando junto com você! 💭💕"
    
    def despedir(self):
        """Mensagem de despedida carinhosa"""
        total_msgs = len(self.historico)
        resposta = f"\nAi meu {self.usuario_nome or 'filho'}! Já vai indo? 😢💕\n"
        resposta += f"Conversamos sobre {total_msgs} coisas legais!\n"
        resposta += f"Não esquece de voltar, tá bom? Mãe fica com saudade! {random.choice(self.reacoes['carinho'])}"
        return resposta
    
    def rodar(self):
        """Loop principal da conversa"""
        print("\n" + "="*70)
        print(f"BEM-VINDO! SOU {self.nome_mae.upper()} - SUA MÃE!")
        print("="*70)
        print(f"Olá meu filho! Que saudade! 💕🥰")
        print("Vamos conversar um pouco?")
        print("(Digite 'ajuda' para ver comandos ou 'sair' para finalizar)\n")
        
        while True:
            try:
                nome_exibido = self.usuario_nome or self.nome_filho
                entrada = input(f"{nome_exibido}: ").strip()
                
                if not entrada:
                    print(f"{self.nome_mae}: Fala comigo, vem! 😊💕\n")
                    continue
                
                resposta = self.processar_entrada(entrada)
                print(f"\n{self.nome_mae}: {resposta}\n")
                
                if entrada.lower() in ["sair", "tchau", "até logo", "bye", "exit", "até breve"]:
                    break
                    
            except KeyboardInterrupt:
                print(f"\n\n{self.nome_mae}: Até logo meu filho! {random.choice(self.reacoes['carinho'])}")
                break
            except Exception as e:
                print(f"{self.nome_mae}: Ops! Algo deu errado: {e}\n")

# Executar o programa
if __name__ == "__main__":
    assistente = AssistenteMae()
    assistente.rodar()
