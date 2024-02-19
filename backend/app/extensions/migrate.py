from flask_migrate import Migrate
from ..models.model import db
from app.models.user_model import User
from app.models.category_model import Category
from app.models.task_model import Task


def init_app(app):
    db.init_app(app)
    Migrate(app, db)
    with app.app_context():
        db.create_all()
        if User.query.first() is None:
            users = [
                User(
                    id=1,
                    name="user test",
                    email="usertest@example.com",
                    password="pbkdf2:sha256:600000$z94gtTytvBBxIgGZ$75e1ad1a0abbeb062943b2ac8f660ae7a69c37f51bad98f654e89e0d2a93048b",
                ),
            ]

            for user in users:
                db.session.add(user)

            category_data = [
                {"name": "Trabalho / Profissional"},
                {"name": "Estudos / Educação"},
                {"name": "Saúde e Bem-estar"},
                {"name": "Finanças"},
                {"name": "Casa e Organização"},
                {"name": "Pessoal / Lazer"},
                {"name": "Desenvolvimento Pessoal"},
                {"name": "Compras"},
                {"name": "Social / Comunitário"},
                {"name": "Digital"},
                {"name": "Outros"},
                {"name": "Importantes"},
            ]

            for category_info in category_data:
                category = Category(name=category_info["name"])
                db.session.add(category)

            task_data = [
                {
                    "category_id": 2,
                    "title": "Organizar reunião de equipe",
                    "description": "Agendar reunião semanal para discutir o progresso do projeto.",
                },
                {
                    "category_id": 2,
                    "title": "Atualizar plano de projeto",
                    "description": "Revisar e atualizar os marcos do projeto para o próximo mês.",
                },
                {
                    "category_id": 3,
                    "title": "Preparar para exame de certificação",
                    "description": "Estudar capítulos 4 e 5 do material de estudo para a certificação.",
                },
                {
                    "category_id": 4,
                    "title": "Marcar consulta médica",
                    "description": "Agendar consulta de rotina com médico de família.",
                },
                {
                    "category_id": 5,
                    "title": "Revisar finanças pessoais",
                    "description": "Analisar despesas e receitas do último mês e ajustar orçamento.",
                },
                {
                    "category_id": 6,
                    "title": "Organizar o escritório",
                    "description": "Limpar e organizar a área de trabalho para melhorar a produtividade.",
                },
                {
                    "category_id": 7,
                    "title": "Planejar viagem de férias",
                    "description": "Pesquisar destinos, voos e acomodações para as próximas férias.",
                },
                {
                    "category_id": 8,
                    "title": "Ler um livro sobre desenvolvimento pessoal",
                    "description": "Escolher e começar a ler um livro recomendado sobre crescimento pessoal.",
                },
                {
                    "category_id": 9,
                    "title": "Fazer compras de supermercado",
                    "description": "Criar uma lista de compras com base no planejamento de refeições para a semana.",
                },
                {
                    "category_id": 10,
                    "title": "Voluntariar em uma organização local",
                    "description": "Pesquisar oportunidades de voluntariado e se inscrever para participar.",
                },
                {
                    "category_id": 11,
                    "title": "Atualizar segurança digital",
                    "description": "Revisar e atualizar senhas e configurações de segurança em contas online.",
                },
                {
                    "category_id": 12,
                    "title": "Organizar documentos importantes",
                    "description": "Separar e arquivar documentos importantes, como contratos e garantias.",
                },
                {
                    "category_id": 1,
                    "title": "Definir metas do ano",
                    "description": "Estabelecer objetivos pessoais e profissionais claros para o ano.",
                },
                {
                    "title": "Completar o relatório anual",
                    "description": "Finalizar a compilação dos resultados anuais para apresentação à diretoria.",
                    "category_id": 2,
                },
                {
                    "title": "Revisar notas de aula de Biologia",
                    "description": "Organizar e revisar as notas de aula para o exame final.",
                    "category_id": 3,
                },
                {
                    "title": "Marcar consulta de rotina",
                    "description": "Agendar uma consulta de rotina com o clínico geral para check-up anual.",
                    "category_id": 4,
                },
                {
                    "title": "Planejar orçamento familiar",
                    "description": "Criar um plano de orçamento para o próximo mês, incluindo todas as despesas fixas e variáveis.",
                    "category_id": 5,
                },
                {
                    "title": "Organizar a despensa",
                    "description": "Verificar validades e organizar os itens por categoria na despensa.",
                    "category_id": 6,
                },
                {
                    "title": "Ler um livro",
                    "description": "Escolher e começar a ler um novo livro de interesse pessoal.",
                    "category_id": 7,
                },
                {
                    "title": "Praticar um novo idioma",
                    "description": "Dedicar 30 minutos diários para praticar um idioma estrangeiro.",
                    "category_id": 8,
                },
                {
                    "title": "Lista de compras do supermercado",
                    "description": "Preparar uma lista de compras para a próxima ida ao supermercado.",
                    "category_id": 9,
                },
                {
                    "title": "Participar de evento comunitário",
                    "description": "Verificar eventos locais e participar de uma atividade comunitária este mês.",
                    "category_id": 10,
                },
                {
                    "title": "Atualizar softwares",
                    "description": "Verificar e instalar atualizações pendentes para softwares no computador pessoal.",
                    "category_id": 11,
                },
                {
                    "title": "Planejar viagem de férias",
                    "description": "Pesquisar destinos, hospedagens e atividades para as próximas férias.",
                    "category_id": 12,
                },
                {
                    "title": "Renovar documentos pessoais",
                    "description": "Verificar a validade do RG, CNH e passaporte e renovar os que estiverem próximos de expirar.",
                    "category_id": 1,
                },
                {
                    "title": "Preparar apresentação para cliente",
                    "description": "Desenvolver slides e material de apoio para reunião com cliente importante na próxima semana.",
                    "category_id": 2,
                },
                {
                    "title": "Concluir projeto de pesquisa",
                    "description": "Finalizar a escrita e revisão do projeto de pesquisa para a disciplina de História.",
                    "category_id": 3,
                },
                {
                    "title": "Iniciar rotina de exercícios",
                    "description": "Definir e começar uma nova rotina de exercícios focada em saúde cardiovascular.",
                    "category_id": 4,
                },
                {
                    "title": "Consultar um planejador financeiro",
                    "description": "Marcar uma consulta com um planejador financeiro para revisar investimentos.",
                    "category_id": 5,
                },
                {
                    "title": "Limpar o escritório",
                    "description": "Fazer uma limpeza completa no escritório, incluindo organização de documentos.",
                    "category_id": 6,
                },
                {
                    "title": "Planejar uma noite de jogos",
                    "description": "Organizar uma noite de jogos de tabuleiro com amigos ou família.",
                    "category_id": 7,
                },
                {
                    "title": "Curso online de fotografia",
                    "description": "Começar um curso online para aprender técnicas básicas de fotografia.",
                    "category_id": 8,
                },
                {
                    "title": "Pesquisar novos gadgets",
                    "description": "Pesquisar os últimos lançamentos em tecnologia e eletrônicos para atualizar os gadgets.",
                    "category_id": 9,
                },
            ]

            for task_info in task_data:
                task = Task(
                    category_id=task_info["category_id"],
                    title=task_info["title"],
                    description=task_info["description"],
                    user_id=1,
                )
                db.session.add(task)

            db.session.commit()
