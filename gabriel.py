import cherrypy


class PaginaGabriel():

    # a professora viu o erro e autorizou a gambiarra
    @cherrypy.expose()
    def index(self):
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/css/gabriel.css">
    <title>Portifólio</title>
</head>
<body>
    <header class="head_cont">
        <div class="header">
            <div class="checkbox">
                <div class="wrapper">
                    <input type="checkbox" id="toggle">
                    <label class="checkbox" for="toggle">
                        <div class="trace"></div>
                        <div class="trace"></div>
                        <div class="trace"></div>
                    </label>
                    <div class="menu"></div>
                    <nav class="menu_item">
                        <ul>
                            <li>
                                <a href="https://www.facebook.com/gabrielyuji.suiama" target="_blank">Facebook</a>
                                <br>
                                <br>
                            </li>
                            <li>
                                <a href="https://www.instagram.com/yujisuiama/" target="_blank">Instagram</a>
                                <br>
                                <br>
                            </li>
                            <li>
                                <a href="https://www.linkedin.com/in/gabriel-yuji-suiama-437373249/" target="_blank">Linkedin</a>
                            </li>
                        </ul>
                    </nav>
                </div>
            </div>
        </div>
        <h1 class="port">🌐Portifólio🌐</h1>
        <h1>Gabriel Yuji Suiama</h1>
        <h2>🍥Japonês🎎</h2>
        <h3>Tel: (18)99657-0104</h3>
        <div class="social">
            <a href="#Hobby">Hobby</a>
            <a href="#Sobre">Sobre</a>
            <a href="#Vida">Vida</a>
        </div>
        <h3>Olá, me chamo Gabriel e este é um portifólio sobre um japonês🍚 que joga vôlei🏐 e ama suas porquinhas🐹!!</h3>
        
    </header>

    <main class="cont">
        <section id="Hobby"></section>
        <div class="card_container">
            <div class="card">
                <div class="card_wrapper">
                    <h2>Hobby</h2>
                    <p>Vem ver!</p>
                </div>
            </div>
            <div class="card_text">
                <div><br>
                    Amo DEMAIS jogar vôlei!!! amo fazer muitas outras coisas também, porém no momento estou jogando somente vôlei, um tempo atrás quando estava no Japão, amava fazer snowboarding, patinar no gelo, boliche e muito mais coisas que davam para ter uma resenha massa com os parceiros.
                </div> 
            </div>
        </div>
        <br>
        <br>
        <br>
        <hr width="75%">
        <section id="Sobre"></section>
        <div class="card_container">
            <div class="card">
                <div class="card_wrapper">
                    <h2>Sobre</h2>
                    <p>Vem ver!</p>
                </div>
            </div>
            <div class="card_text"><br>
                Eu nasci no Brasil em Presidente Prudente no dia 1 de Abril de 2003. Sou "descendente japonês" 4º geração, tenho uma irmã gêmea. Minha altura é de 1,69m aproximadamente, peso 75kg, tipo sanguineo +O.
            </div>
        </div>
        <br>
        <br>
        <br>
        <hr width="75%">
        
        <section id="Vida"></section>
        <div class="card_container">
            <div class="card">
                <div class="card_wrapper">
                    <h2>Vida</h2>
                    <p>Vem ver!</p>
                </div>
            </div>
            <div class="card_text"><br>
                Aos 4 anos de idade fui para o Japão, visitei 2 vezes o Brasil, uma quando tinha 8 anos e a outra quando tinha 12 anos. Voltei do Japão no dia 30 de janeiro de 2022, desde então estou me acostumando de pouco a pouco, definitivamente o que mais me ajudou nesse momento agitado da minha vida foi o vôlei.
            </div>
        </div>
    </main>

    <footer class="pe">
        Feito por Gabriel Yuji Suiama RA: 262228092
    </footer>
    <a id="link-topo" href="#">&#9650;</a>
</body>
</html>'''

        return html
