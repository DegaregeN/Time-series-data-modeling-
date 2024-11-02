# Time series data modeling

Time_series_data_modeling/

├── data/

│   ├── raw/                      # Raw data files (e.g., historical oil prices)

│   ├── processed/                # Processed data ready for analysis

│   ├── external/                 # External data sources 

│   └── README.md                 # Description of data files and sources
│

├── notebooks/

│   ├── 01-data-preprocessing.ipynb      # Data cleaning and preprocessing steps

│   ├── 02-exploratory-data-analysis.ipynb # EDA with visualizations

│   ├── 03-time-series-analysis.ipynb      # Time series modeling (ARIMA, GARCH)

│   ├── 04-advanced-models.ipynb           # Advanced models (VAR, LSTM)

│   └── README.md                         # Overview of notebooks
│
├── src/                           # Source code for data preprocessing, feature engineering, and modeling
│   ├── data_preprocessing.py      # Preprocess data and save processed data
│   ├── feature_engineering.py     # Add features to the processed data
│   ├── model_building.py          # Model building functions (ARIMA, GARCH, LSTM)
│   ├── evaluation.py              # Evaluate models with metrics like RMSE, MAE
│   └── README.md                  # Overview of scripts
│
├── models/                        # Saved models for further use or evaluation
│   ├── baseline/                  # Baseline models (e.g., ARIMA, GARCH)
│   ├── advanced/                  # Advanced models (e.g., LSTM, VAR)
│   └── README.md                  # Model details and evaluation results
│
├── dashboard/                     # Flask and React dashboard for interactive analysis
│   ├── backend/                   # Flask API backend
│   │   ├── app.py                 # Flask API for data and models
│   │   ├── config.py              # Configuration settings for backend
│   │   ├── routes/                # API route definitions
│   │   └── README.md              # Backend overview
│   ├── frontend/                  # React frontend
│   │   ├── src/                   # Source folder for React app
│   │   ├── public/                # Public assets and static files
│   │   ├── components/            # React components (charts, filters)
│   │   └── README.md              # Frontend overview
│   └── README.md                  # Dashboard overview
│
├── reports/                       # Documentation, reports, and presentation materials
│   ├── research-papers/           # Relevant journal articles and references
│   ├── presentation/              # Slide decks and presentation files
│   ├── analysis-summary.md        # Summary of analysis and insights
│   └── README.md                  # Documentation overview
│
├── requirements.txt               # Python package requirements
├── README.md                      # Project overview
├── LICENSE                        # Project license
└── .gitignore                     # Files to ignore in Git
