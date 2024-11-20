import os
import sys
import time
import random
import ipaddress
from typing import List, Dict, Optional
from dataclasses import dataclass

# Função global para limpar a tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para sons
def play_sound(frequency=440, duration=0.1):
    """Reproduz um som usando caracteres especiais"""
    if os.name == 'nt':  # Windows
        try:
            import winsound
            winsound.Beep(frequency, int(duration * 1000))
        except:
            print('\a', end='', flush=True)
    else:  # Linux/Mac/Android
        print('\x07', end='', flush=True)
        time.sleep(duration)

CYBER_LOGO = """
█░█ █▀▀ █▄▀ ▀█▀ █▀█ █▀█   █▀█ █▀
▀▄▀ ██▄ █░█ ░█░ █▄█ █▀▄   █▄█ ▄█  v2.1.0
"""

COMING_SOON_ART = """
╔══════════════════════════════════════════════╗
║       ╔═╗╔═╗╔╦╗╦╔╗╔╔═╗  ╔═╗╔═╗╔═╗╔╗╔         ║
║       ║  ║ ║║║║║║║║║ ╦  ╚═╗║ ║║ ║║║║         ║
║       ╚═╝╚═╝╩ ╩╩╝╚╝╚═╝  ╚═╝╚═╝╚═╝╝╚╝         ║
║                                              ║
║        [DISPONÍVEL NA VERSÃO v2.2.0]         ║
║     [AGUARDE AS PRÓXIMAS ATUALIZAÇÕES]       ║
╚══════════════════════════════════════════════╝
"""

@dataclass
class HackType:
    code: str
    name: str
    coming_soon: bool = False

HACK_TYPES = [
    HackType("DAEMON_BREACH", "Quebra de Daemon Neural"),
    HackType("NEURAL_BYPASS", "Bypass Neural [v2.2.0]", True),
    HackType("DARKNET_DIVE", "Mergulho na Darknet [v2.2.0]", True),
    HackType("QUANTUM_CRACK", "Decodificador Quântico")
]

# Cores ANSI para terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

# Sons aprimorados
class Sound:
    @staticmethod
    def beep():
        play_sound(800, 0.1)
        
    @staticmethod
    def error():
        play_sound(400, 0.1)
        time.sleep(0.1)
        play_sound(300, 0.2)
    
    @staticmethod
    def success():
        play_sound(800, 0.1)
        time.sleep(0.1)
        play_sound(1000, 0.1)
        time.sleep(0.1)
        play_sound(1200, 0.2)
    
    @staticmethod
    def alert():
        for _ in range(3):
            play_sound(600, 0.2)
            time.sleep(0.1)

    @staticmethod
    def startup():
        freqs = [400, 600, 800, 1000]
        for freq in freqs:
            play_sound(freq, 0.1)
            time.sleep(0.05)

    @staticmethod
    def shutdown():
        freqs = [1000, 800, 600, 400]
        for freq in freqs:
            play_sound(freq, 0.1)
            time.sleep(0.05)

class MenuManager:
    def print_menu(self, options: List[str]):
        for i, option in enumerate(options, 1):
            print(Colors.CYAN + f"  [{i}] " + option + Colors.END)

    def menu_selection(self, options: List[str], header: str = "SELECIONE UMA OPÇÃO") -> int:
        while True:
            clear_screen()  # Usando função global
            print(Colors.GREEN + CYBER_LOGO)
            print(Colors.CYAN + "="*60)
            print(Colors.GREEN + header.center(60))
            print(Colors.CYAN + "="*60 + "\n")
            
            self.print_menu(options)
            print("\n" + Colors.YELLOW + "[DIGITE O NÚMERO DA OPÇÃO DESEJADA]" + Colors.END)
            
            try:
                choice = input(Colors.CYAN + ">>> " + Colors.END)
                selected = int(choice) - 1
                if 0 <= selected < len(options):
                    Sound.beep()
                    return selected
                else:
                    Sound.error()
            except ValueError:
                Sound.error()
class CyberTerminal:
    def __init__(self):
        self.running = True
        self.current_hack = None
        self.menu_manager = MenuManager()

    def print_fast(self, text: str, color=Colors.CYAN, delay: float = 0.001):
        for char in text:
            print(color + char + Colors.END, end='', flush=True)
            if not char.isspace():
                time.sleep(delay)
                if random.random() < 0.1:  # 10% de chance de fazer beep durante a digitação
                    play_sound(random.randint(800, 1200), 0.01)
        print()

    def display_coming_soon(self) -> bool:
        clear_screen()
        Sound.alert()
        print(Colors.YELLOW + COMING_SOON_ART)
        print(Colors.YELLOW + "[PRESSIONE ENTER PARA VOLTAR]")
        input()
        return False

    def startup_sequence(self):
        clear_screen()
        Sound.startup()
        
        startup_text = [
            "[INICIANDO VEKTOR_OS 2077]",
            "[CARREGANDO DRIVERS NEURAIS...]",
            "[INTERFACE BIOMECÂNICA ONLINE]",
            "[CONECTANDO À MATRIX GLOBAL...]",
            "[BYPASSANDO PROTOCOLOS ICE...]",
            "[PROTOCOLOS DE SEGURANÇA ATIVOS]",
            "[BEM-VINDO À MATRIX, RUNNER]"
        ]
        
        for line in CYBER_LOGO.split('\n'):
            self.print_fast(line, Colors.GREEN, delay=0.1)
            
        for text in startup_text:
            self.print_fast(text)
            Sound.beep()
            time.sleep(0.2)
        
        time.sleep(0.5)
        clear_screen()

    def main_menu(self) -> int:
        options = [
            "Iniciar Exploit",
            "Desconectar do SO"
        ]
        return self.menu_manager.menu_selection(options, "THE ULTIMATE NEURAL HACKING TOOL")

    def select_hack_type(self) -> bool:
        options = [hack.name for hack in HACK_TYPES]
        selected = self.menu_manager.menu_selection(options, "SELECIONE O EXPLOIT")
        self.current_hack = HACK_TYPES[selected]
        
        if self.current_hack.coming_soon:
            return self.display_coming_soon()
        return True

    @staticmethod
    def roll_dice(num_dice: int) -> List[int]:
        return [random.randint(1, 6) for _ in range(num_dice)]

    @staticmethod
    def generate_random_ip() -> str:
        return str(ipaddress.IPv4Address(random.randint(0, 2**32 - 1)))

    @staticmethod
    def generate_security_code() -> str:
        chars = "0123456789ABCDEF"
        return "-".join(
            "".join(random.choice(chars) for _ in range(4))
            for _ in range(3)
        )

    def display_rolling_animation(self, final_rolls: List[int]):
        loading_chars = ["■", "□"]
        bar_size = 30
        
        def create_loading_bar(progress: float) -> str:
            filled = int(bar_size * progress)
            bar = "".join(loading_chars[0] if i < filled else loading_chars[1] for i in range(bar_size))
            return f"[{bar}] {int(progress * 100)}%"

        try:
            steps = 30
            for i in range(steps + 1):
                progress = i / steps
                clear_screen()
                print(Colors.GREEN + f"[EXECUTANDO {self.current_hack.name}]")
                print(Colors.CYAN + create_loading_bar(progress))
                print(Colors.YELLOW + "\n[INICIALIZANDO MÓDULOS DE INTRUSÃO]")
                if i % 3 == 0:  # Aumentei a frequência dos beeps
                    play_sound(400 + (i * 20), 0.1)  # Tom aumenta gradualmente
                time.sleep(0.1)
            
            for _ in range(3):
                for color in [Colors.RED, Colors.CYAN]:
                    clear_screen()
                    print(Colors.GREEN + f"[EXECUTANDO {self.current_hack.name}]")
                    print(color + create_loading_bar(1.0))
                    print(Colors.YELLOW + "\n[PROCESSANDO DADOS...]")
                    Sound.beep()
                    time.sleep(0.1)

            clear_screen()
            print(Colors.GREEN + f"[EXECUTANDO {self.current_hack.name}]")
            print(Colors.GREEN + create_loading_bar(1.0))
            print(Colors.YELLOW + f"\n[RESULTADO DA INTRUSÃO]: {final_rolls}")
            Sound.success()
            time.sleep(1)
            print("\n" + Colors.YELLOW + "[PRESSIONE ENTER PARA CONTINUAR]")
            input()
            
        except Exception as e:
            raise e
    def simulate_hack_attempt(self):
        if not self.select_hack_type():
            return
        
        clear_screen()
        self.print_fast(f"[INICIANDO {self.current_hack.name}]", Colors.GREEN)
        print(Colors.CYAN + "[DIGITE NÚMERO DE MÓDULOS DE INTRUSÃO (1-10)] >>> ", end="")
        
        try:
            num_dice = int(input())
            if not 1 <= num_dice <= 10:
                raise ValueError
            Sound.beep()
        except ValueError:
            Sound.error()
            print(Colors.RED + "[ERRO] Número inválido de módulos. Pressione Enter...")
            input()
            return
        
        rolls = self.roll_dice(num_dice)
        max_roll = max(rolls) if rolls else 0
        
        self.display_rolling_animation(rolls)
        
        if self.current_hack.code == "QUANTUM_CRACK":
            if max_roll >= 5:
                Sound.success()
                self.quantum_crack_success(max_roll)
            else:
                Sound.alert()
                self.display_failure()
        else:
            success_count = sum(1 for roll in rolls if roll >= 5)
            critical_success = any(roll == 6 for roll in rolls)
            
            if critical_success:
                Sound.success()
                self.display_success()
            elif success_count > 0:
                Sound.beep()
                self.display_partial_success()
            else:
                Sound.alert()
                self.display_failure()

    def display_success(self):
        messages = [
            "╔══════════════════════════════╗",
            "║     ACESSO TOTAL OBTIDO      ║",
            "╚══════════════════════════════╝",
            "[FIREWALL NEUTRALIZADO]",
            "[DADOS BAIXADOS COM SUCESSO]",
            "[ADMINISTRADOR ROOT OBTIDO]",
            f"[IP MASCARADO]: {self.generate_random_ip()}",
            "[RASTROS DIGITAIS ELIMINADOS]"
        ]
        
        clear_screen()
        for msg in messages:
            self.print_fast(msg, Colors.GREEN)
            play_sound(random.randint(800, 1200), 0.05)
            time.sleep(0.2)
        
        print("\n" + Colors.YELLOW + "[PRESSIONE ENTER PARA CONTINUAR]")
        input()

    def display_partial_success(self):
        messages = [
            "╔══════════════════════════════╗",
            "║    ACESSO PARCIAL OBTIDO     ║",
            "╚══════════════════════════════╝",
            "[ALERTA: DETECÇÃO PARCIAL]",
            "[SISTEMAS DE SEGURANÇA ATIVOS]",
            f"[IP DETECTADO]: {self.generate_random_ip()}",
            "[FIREWALL PARCIALMENTE ATIVO]"
        ]
        
        clear_screen()
        for msg in messages:
            self.print_fast(msg, Colors.YELLOW)
            play_sound(random.randint(600, 1000), 0.05)
            time.sleep(0.2)
        
        print("\n" + Colors.YELLOW + "[PRESSIONE ENTER PARA CONTINUAR]")
        input()

    def display_failure(self):
        clear_screen()
        messages = [
            "╔══════════════════════════════╗",
            "║      !!! ALERTA !!!          ║",
            "╚══════════════════════════════╝",
            "[FALHA CRÍTICA DE ACESSO]",
            "[ICE BLACK DETECTADO]",
            "[CONTRAMEDIDAS ATIVADAS]",
            f"[IP COMPROMETIDO]: {self.generate_random_ip()}",
            "[ALERTANDO NETWATCH...]",
            "[TRAÇADORES CORPORATIVOS ATIVOS]"
        ]
        
        for msg in messages:
            self.print_fast(msg, Colors.RED)
            play_sound(random.randint(300, 600), 0.1)
            time.sleep(0.2)
        
        print("\n" + Colors.YELLOW + "[PRESSIONE ENTER PARA CONTINUAR]")
        input()

    def quantum_crack_success(self, max_roll):
        if max_roll == 6:
            correct_code = self.generate_security_code()
            messages = [
                "╔═════════════════════════════════════╗",
                "║    DECODIFICAÇÃO QUÂNTICA: ÊXITO    ║",
                "╚═════════════════════════════════════╝",
                "[SENHA DECODIFICADA COM SUCESSO]",
                f"[CÓDIGO DE ACESSO]: {correct_code}",
                "[ACESSO GARANTIDO]"
            ]
            
            clear_screen()
            for msg in messages:
                self.print_fast(msg, Colors.GREEN)
                play_sound(random.randint(800, 1200), 0.05)
                time.sleep(0.2)
            
            print("\n" + Colors.YELLOW + "[PRESSIONE ENTER PARA CONTINUAR]")
            input()
                
        elif max_roll == 5:
            correct_code = self.generate_security_code()
            fake_codes = [self.generate_security_code() for _ in range(3)]
            all_codes = fake_codes + [correct_code]
            random.shuffle(all_codes)
            
            clear_screen()
            messages = [
                "╔═════════════════════════════════════╗",
                "║    DECODIFICAÇÃO PARCIAL: ALERTA    ║",
                "╚═════════════════════════════════════╝",
                "[SEQUÊNCIAS POTENCIAIS DETECTADAS]",
                "[VOCÊ TEM 3 TENTATIVAS]"
            ]
            
            for msg in messages:
                self.print_fast(msg, Colors.YELLOW)
                play_sound(random.randint(600, 1000), 0.05)
                time.sleep(0.2)
            
            print("\n" + Colors.YELLOW + "[PRESSIONE ENTER PARA CONTINUAR]")
            input()
            
            attempts = 3
            while attempts > 0:
                selected = self.select_code_menu(all_codes, attempts)
                selected_code = all_codes[selected]
                
                if selected_code == correct_code:
                    Sound.success()
                    messages = [
                        "╔═════════════════════════════════════╗",
                        "║         CÓDIGO CORRETO!!!           ║",
                        "╚═════════════════════════════════════╝",
                        "[DECODIFICAÇÃO BEM-SUCEDIDA]",
                        f"[CÓDIGO VALIDADO]: {selected_code}",
                        "[ACESSO GARANTIDO]"
                    ]
                    clear_screen()
                    for msg in messages:
                        self.print_fast(msg, Colors.GREEN)
                        play_sound(random.randint(800, 1200), 0.05)
                        time.sleep(0.2)
                    print("\n" + Colors.YELLOW + "[PRESSIONE ENTER PARA CONTINUAR]")
                    input()
                    return
                else:
                    Sound.error()
                    attempts -= 1
                    if attempts > 0:
                        error_messages = [
                            "╔═════════════════════════════════════╗",
                            "║         CÓDIGO INCORRETO!           ║",
                            "╚═════════════════════════════════════╝",
                            f"[TENTATIVAS RESTANTES]: {attempts}"
                        ]
                        clear_screen()
                        for msg in error_messages:
                            self.print_fast(msg, Colors.RED)
                            play_sound(random.randint(300, 600), 0.1)
                            time.sleep(0.2)
                        print("\n" + Colors.YELLOW + "[PRESSIONE ENTER PARA CONTINUAR]")
                        input()
                    else:
                        Sound.alert()
                        self.display_failure()

    def select_code_menu(self, codes: List[str], attempts_left: int) -> int:
        while True:
            clear_screen()
            print(Colors.CYAN + "╔═════════════════════════════════════╗")
            print(Colors.CYAN + "║    SELECIONE O CÓDIGO DE ACESSO     ║")
            print(Colors.CYAN + "╚═════════════════════════════════════╝\n")
            
            print(Colors.GREEN + f"[TENTATIVAS RESTANTES]: {attempts_left}\n")
            
            for i, code in enumerate(codes, 1):
                print(Colors.CYAN + f"  [{i}] {code}")
            
            print("\n" + Colors.YELLOW + "[DIGITE O NÚMERO DO CÓDIGO]")
            
            try:
                choice = input(Colors.CYAN + ">>> " + Colors.END)
                selected = int(choice) - 1
                if 0 <= selected < len(codes):
                    Sound.beep()
                    return selected
                Sound.error()
            except ValueError:
                Sound.error()

    def run(self):
        self.startup_sequence()
        while self.running:
            choice = self.main_menu()
            if choice == 0:  # Iniciar Exploit
                self.simulate_hack_attempt()
            else:  # Desconectar da Matrix
                self.running = False
                clear_screen()
                self.print_fast("[DESCONECTANDO DA MATRIX...]", Colors.CYAN)
                Sound.shutdown()
                print("\n" + Colors.YELLOW + "[PRESSIONE ENTER PARA CONFIRMAR DESCONEXÃO]")
                input()
                clear_screen()
                self.print_fast("[CONEXÃO ENCERRADA - ATÉ A PRÓXIMA, RUNNER]", Colors.RED)
                Sound.alert()
                time.sleep(2)
                break

def main():
    try:
        terminal = CyberTerminal()
        terminal.run()
    except KeyboardInterrupt:
        print("\n" + Colors.RED + "[DESCONEXÃO FORÇADA]" + Colors.END)
        Sound.alert()
        sys.exit(0)
    except Exception as e:
        print(Colors.RED + f"[ERRO CRÍTICO]: {str(e)}" + Colors.END)
        Sound.error()
        sys.exit(1)

if __name__ == "__main__":
    main()