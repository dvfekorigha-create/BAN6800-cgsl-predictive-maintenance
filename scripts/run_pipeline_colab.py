# Colab helper: after Module 3 files are uploaded to GitHub, clone and run the pipeline.
REPO = 'https://github.com/dvfekorigha-create/BAN6800-cgsl-predictive-maintenance.git'

def commands():
    return [
        f'git clone {REPO}',
        'cd BAN6800-cgsl-predictive-maintenance',
        'pip install -r requirements.txt',
        'python scripts/run_pipeline.py',
        'pytest -q tests',
    ]

if __name__ == '__main__':
    print('\n'.join(commands()))
