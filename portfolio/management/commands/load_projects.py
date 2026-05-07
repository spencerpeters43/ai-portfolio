import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings
from portfolio.models import Project

ASSETS_BASE = os.path.join(settings.BASE_DIR, 'portfolio_assets:')
SCREENSHOTS_SRC = os.path.join(ASSETS_BASE, 'screenshots:')
VIDEOS_SRC = os.path.join(ASSETS_BASE, 'videos:')
DOWNLOADS_SRC = os.path.join(ASSETS_BASE, 'downloads:')

PROJECTS = [
    {
        'title': 'AI Portfolio Assistant Chatbot',
        'slug': 'ai-portfolio-assistant-chatbot',
        'summary': (
            'Designed and developed an AI-powered portfolio chatbot to guide users through a '
            'personal project website, answer questions about projects and experience, and improve '
            'user interaction through conversational AI.'
        ),
        'project_type': 'chatbot',
        'business_problem': (
            'Traditional websites are static and require users to manually search for information. '
            'This project addresses the need for a more interactive and personalized user experience '
            'by using AI to provide instant navigation assistance and contextual responses about '
            'technical projects and professional experience.'
        ),
        'tools_used': 'Botpress',
        'key_features': (
            'Conversational AI assistant embedded directly into the portfolio homepage\n'
            'Website navigation assistance for users exploring projects and experience\n'
            'AI-generated responses trained on portfolio content and project information'
        ),
        'my_role': 'Sole Developer',
        'biggest_challenge': (
            'Designing a chatbot capable of providing accurate, concise, and context-aware responses '
            'while maintaining a professional user experience. Another challenge was structuring '
            'website content in a way that could be effectively leveraged by the AI knowledge base.'
        ),
        'what_i_learned': (
            'Learned how conversational AI systems can enhance user engagement and automate '
            'information delivery within web applications. Developed experience with chatbot workflow '
            'design, prompt engineering, AI training strategies, and integrating automation into a '
            'professional-facing platform.'
        ),
        'github_link': '',
        'live_demo_link': (
            'https://cdn.botpress.cloud/webchat/v3.6/shareable.html'
            '?configUrl=https://files.bpcontent.cloud/2026/05/07/00/20260507005027-JOO0N42C.json'
        ),
        'screenshot': '',
        'video': '',
        'downloadable_file': '',
        'is_featured': True,
        'order': 1,
    },
    {
        'title': 'AI-Powered Handyman Service Automation Workflow',
        'slug': 'ai-powered-handyman-service-automation-workflow',
        'summary': (
            'Developed an automated AI workflow that streamlined service intake, pricing, scheduling, '
            'and customer communication for a handyman business using intelligent workflow automation.'
        ),
        'project_type': 'workflow',
        'business_problem': (
            'Small service businesses often rely on manual coordination for customer intake, pricing '
            'estimates, scheduling, and communication, which can be time-consuming and inconsistent. '
            'This project automated these operational tasks to improve efficiency, response speed, '
            'and customer experience.'
        ),
        'tools_used': 'n8n\nGoogle Forms\nGoogle Sheets\nGemini API',
        'key_features': (
            'Automated customer intake through Google Forms\n'
            'Trigger-based workflow orchestration using n8n\n'
            'AI-assisted pricing estimation for maintenance requests\n'
            'Automated scheduling recommendations based on availability data\n'
            'Dynamic customer confirmation emails with pricing and scheduling details\n'
            'Structured JSON data flow between workflow components and AI systems\n'
            'AI-generated plain-English customer communication'
        ),
        'my_role': 'Sole Developer',
        'biggest_challenge': (
            'The most significant challenge was engineering reliable AI-generated customer emails. '
            'The workflow required converting structured JSON outputs into professionally formatted, '
            'natural-language responses using Gemini. Achieving consistent formatting and accurate '
            'communication required extensive prompt engineering.'
        ),
        'what_i_learned': (
            'Developed practical experience with AI workflow orchestration, API-based automation, '
            'prompt engineering, and structured data pipelines. Learned how large language models '
            'can be integrated into operational business workflows to automate customer communication '
            'and improve service efficiency.'
        ),
        'github_link': '',
        'live_demo_link': '',
        'screenshot': 'screenshots/n8n_workflow.png',
        'video': '',
        'downloadable_file': 'downloads/n8n_workflow.json',
        'is_featured': True,
        'order': 2,
    },
    {
        'title': 'LangChain Conversational AI Assistant',
        'slug': 'langchain-conversational-ai-assistant',
        'summary': (
            'Built a terminal-based conversational AI application using LangChain and the Gemini API '
            'to demonstrate how large language models can be integrated into Python applications with '
            'persistent conversational memory.'
        ),
        'project_type': 'code',
        'business_problem': (
            'Many organizations want to integrate AI capabilities into internal tools and applications '
            'but lack practical frameworks for managing conversations, memory, and LLM interactions. '
            'This project explored how conversational AI systems can be embedded into software '
            'environments to support more intelligent and context-aware user interactions.'
        ),
        'tools_used': 'LangChain\nPython\nGemini API',
        'key_features': (
            'Terminal-based conversational AI interface\n'
            'Integration of Gemini LLM into a Python application\n'
            'Persistent conversational memory allowing multi-turn interactions\n'
            'Context-aware responses based on previous prompts\n'
            'Modular AI workflow structure using LangChain'
        ),
        'my_role': 'Sole Developer',
        'biggest_challenge': (
            'One of the primary challenges was implementing conversational memory without repeatedly '
            'reprocessing prior prompts. Solving this required carefully structuring and managing the '
            'dictionaries used to store conversation history and context so the AI could maintain '
            'coherent multi-turn interactions efficiently.'
        ),
        'what_i_learned': (
            'Gained hands-on experience integrating large language models into software applications '
            'using LangChain. Developed a deeper understanding of prompt engineering, conversational '
            'memory, AI application architecture, and how LLM orchestration frameworks simplify the '
            'development of intelligent systems.'
        ),
        'github_link': 'https://github.com/spencerpeters43/LangChainProject.git',
        'live_demo_link': '',
        'screenshot': 'screenshots/langchain.png',
        'video': '',
        'downloadable_file': 'downloads/langchain_agent.zip',
        'is_featured': True,
        'order': 3,
    },
    {
        'title': 'AI-Generated Alternate Movie Scene Project',
        'slug': 'ai-generated-alternate-movie-scene-project',
        'summary': (
            'Created an AI-generated alternate movie scene using Google AI Studio and generative '
            'media tools to reimagine a pivotal moment from Finding Nemo through AI-assisted image '
            'and video generation.'
        ),
        'project_type': 'video',
        'business_problem': (
            'Businesses increasingly require large amounts of digital content for advertising, '
            'branding, social media, and website development, but traditional media production can '
            'be expensive and time-intensive. This project explored how generative AI tools can '
            'accelerate content creation by enabling rapid production of customized visual media '
            'and promotional assets at a significantly lower cost and faster turnaround time.'
        ),
        'tools_used': 'Google AI Studio\nGoogle Image Generation Tools',
        'key_features': (
            'AI-generated storyboard-style still frames\n'
            'Short-form AI-generated cinematic video sequence\n'
            'Alternate plot development for an existing film scene\n'
            'Prompt-driven image and scene generation\n'
            'Consistent visual styling across generated media\n'
            'AI-assisted creative storytelling and scene reconstruction'
        ),
        'my_role': 'Sole Developer',
        'biggest_challenge': (
            'The primary challenge was generating visuals that were stylistically recognizable as '
            'inspired by Finding Nemo while remaining sufficiently original to avoid intellectual '
            'property and trademark concerns. This required careful prompt engineering and iterative '
            'refinement of the generated media outputs.'
        ),
        'what_i_learned': (
            'Learned how generative AI can be applied to creative media production, storyboarding, '
            'and cinematic prototyping. Developed experience with prompt engineering for image and '
            'video generation, visual consistency management, and the ethical considerations '
            'surrounding AI-generated media and intellectual property.'
        ),
        'github_link': '',
        'live_demo_link': '',
        'screenshot': 'screenshots/google_ai_studio.png',
        'video': 'videos/google_ai_studio_demo.mp4',
        'downloadable_file': '',
        'is_featured': True,
        'order': 4,
    },
    {
        'title': 'Handwritten Digit Recognition Machine Learning Model',
        'slug': 'handwritten-digit-recognition-machine-learning-model',
        'summary': (
            'Developed a machine learning model using scikit-learn to classify handwritten numerical '
            'digits and evaluate prediction accuracy using image-based data.'
        ),
        'project_type': 'code',
        'business_problem': (
            'Organizations increasingly use applied machine learning to automate classification, '
            'prediction, and pattern-recognition tasks across industries such as finance, healthcare, '
            'logistics, and technology. This project demonstrated how machine learning models can be '
            'trained to recognize visual patterns and make accurate predictions from data, '
            'highlighting the practical business applications of AI-driven automation and decision '
            'support systems.'
        ),
        'tools_used': 'scikit-learn\nPython',
        'key_features': (
            'Machine learning model training and testing\n'
            'Accuracy evaluation and prediction analysis\n'
            'Data preprocessing for structured model input'
        ),
        'my_role': 'Implemented and tested the model through a guided in-class machine learning exercise.',
        'biggest_challenge': (
            'The primary challenge was understanding how machine learning models interpret image data '
            'and convert visual patterns into numerical predictions. Learning how training data, '
            'preprocessing, and model evaluation interact within the machine learning pipeline '
            'required significant conceptual understanding.'
        ),
        'what_i_learned': (
            'Developed foundational knowledge of traditional machine learning concepts, including '
            'model training, classification, prediction accuracy, and supervised learning workflows. '
            'Gained hands-on experience using scikit-learn and learned how machine learning models '
            'can recognize patterns within structured datasets.'
        ),
        'github_link': 'https://github.com/spencerpeters43/ml_project.git',
        'live_demo_link': '',
        'screenshot': 'screenshots/ml_project.png',
        'video': '',
        'downloadable_file': 'downloads/ml_project.zip',
        'is_featured': True,
        'order': 5,
    },
    {
        'title': 'Campus SkillSwap Django Marketplace',
        'slug': 'campus-skillswap-django-marketplace',
        'summary': (
            'Developed a student-focused marketplace web application using Django and AI-assisted '
            '"vibe coding" workflows to rapidly prototype a platform for sharing skills and services '
            'on campus.'
        ),
        'project_type': 'web_app',
        'business_problem': (
            'Traditional software development can be time-intensive and require significant technical '
            'resources to prototype new business ideas. This project explored how AI-assisted '
            'development and prompt-driven coding workflows can accelerate software creation by '
            'translating business concepts into functional applications more efficiently.'
        ),
        'tools_used': 'Django\nPython\nClaude for VS Code',
        'key_features': (
            'Student marketplace platform for offering skills and services\n'
            'User authentication and authorization system\n'
            'Dynamic listing and navigation functionality\n'
            'AI-assisted rapid application development'
        ),
        'my_role': 'Sole Developer',
        'biggest_challenge': (
            'The most significant challenge was ensuring proper authentication and authorization '
            'controls while maintaining reliable navigation and functionality across all internal '
            'pages and features. This required extensive testing and refinement of both backend '
            'logic and application workflows.'
        ),
        'what_i_learned': (
            'Developed experience with Django web development, authentication systems, and '
            'AI-assisted coding workflows. Learned how prompt engineering can accelerate software '
            'prototyping and how AI tools can be leveraged to rapidly transform business concepts '
            'into functional applications while still requiring careful testing and system validation.'
        ),
        'github_link': 'https://github.com/spencerpeters43/campus_skillswap.git',
        'live_demo_link': 'https://campus-skillswap-6gf4.onrender.com',
        'screenshot': 'screenshots/skillswap.png',
        'video': '',
        'downloadable_file': '',
        'is_featured': True,
        'order': 6,
    },
]


class Command(BaseCommand):
    help = 'Copy portfolio media files and load all 6 projects into the database'

    def handle(self, *args, **options):
        self._copy_media_files()
        self._load_projects()

    def _copy_media_files(self):
        media_screenshots = os.path.join(settings.MEDIA_ROOT, 'screenshots')
        media_videos = os.path.join(settings.MEDIA_ROOT, 'videos')
        media_downloads = os.path.join(settings.MEDIA_ROOT, 'downloads')
        static_img = os.path.join(settings.BASE_DIR, 'static', 'img')

        for dest in [media_screenshots, media_videos, media_downloads, static_img]:
            os.makedirs(dest, exist_ok=True)

        for filename in os.listdir(SCREENSHOTS_SRC):
            src = os.path.join(SCREENSHOTS_SRC, filename)
            if filename == 'profile.jpg':
                shutil.copy(src, os.path.join(static_img, filename))
                self.stdout.write(f'  Copied {filename} → static/img/')
            else:
                shutil.copy(src, os.path.join(media_screenshots, filename))
                self.stdout.write(f'  Copied {filename} → media/screenshots/')

        for filename in os.listdir(VIDEOS_SRC):
            shutil.copy(os.path.join(VIDEOS_SRC, filename), os.path.join(media_videos, filename))
            self.stdout.write(f'  Copied {filename} → media/videos/')

        for filename in os.listdir(DOWNLOADS_SRC):
            shutil.copy(os.path.join(DOWNLOADS_SRC, filename), os.path.join(media_downloads, filename))
            self.stdout.write(f'  Copied {filename} → media/downloads/')

        self.stdout.write(self.style.SUCCESS('Media files copied.'))

    def _load_projects(self):
        Project.objects.all().delete()
        self.stdout.write('Cleared existing projects.')

        for data in PROJECTS:
            Project.objects.create(**data)
            self.stdout.write(f'  Created: {data["title"]}')

        self.stdout.write(self.style.SUCCESS(f'Loaded {len(PROJECTS)} projects successfully.'))
