pipeline {
    agent any

    options {
        timestamps()
        skipDefaultCheckout(false)
        disableConcurrentBuilds()
    }

    parameters {
        string(name: 'SOURCE_CONNECTION', defaultValue: 'SOURCE', description: 'Connection prefix used by the source fixture')
        string(name: 'TARGET_CONNECTION', defaultValue: 'TARGET', description: 'Connection prefix used by the target fixture')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Create virtual environment') {
            steps {
                sh '''
                    set -eux
                    python3 --version
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run smoke database tests') {
            steps {
                // Create the Jenkins credential below as a Secret file containing
                // the same KEY=value entries used by the local .env file.
                withCredentials([file(credentialsId: 'etl-db-env', variable: 'DB_ENV_FILE')]) {
                    sh '''
                        set -eu
                        . .venv/bin/activate
                        cp "$DB_ENV_FILE" .env
                        export SOURCE_CONNECTION="$SOURCE_CONNECTION"
                        export TARGET_CONNECTION="$TARGET_CONNECTION"
                        pytest tests/smoke/01.test_db_connection.py \
                            --junitxml=reports/junit-smoke.xml
                    '''
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/**/*.html, reports/**/*.xml', allowEmptyArchive: true
            junit testResults: 'reports/**/*.xml', allowEmptyResults: true
            sh 'rm -f .env'
        }
        cleanup {
            sh 'rm -rf .venv'
        }
    }
}
