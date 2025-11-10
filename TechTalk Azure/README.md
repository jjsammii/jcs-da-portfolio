# 🎥 Tech Expert Hour — Azure Data Factory & Machine Learning (Fujitsu Caribbean)

**Presenter:** Jermaine (“Jeremy”) Samuels
**Host:** Crystal-Gail Williams — Marketing Officer, Fujitsu Caribbean (Jamaica)

**📺 Watch the Full Session on YouTube:**
👉 [https://www.youtube.com/watch?v=mWW-OsELCn0&t=1400s](https://www.youtube.com/watch?v=mWW-OsELCn0&t=1400s)

This **Tech Expert Hour** session introduces a practical, end-to-end approach for building **cloud business intelligence (BI) pipelines** with **Azure Data Factory (ADF)**, **Azure Machine Learning (Azure ML)**, and **Power BI**.
It covers business context, data orchestration, model training & evaluation, secure connectivity between on-premise and cloud, and the delivery of **interactive analytics** for decision-makers.

> 💡 *"Where there's data, there's value."* — The session explores how modern organizations can transform raw data into strategic advantage by progressing from **descriptive** to **predictive** and **prescriptive** analytics.

---

## 🎯 What You’ll Learn

* 🌐 **Cloud BI Simplified:** How cloud computing accelerates insight delivery across teams and devices
* 📊 **Analytics Maturity Curve:** Descriptive → Diagnostic → Predictive → Prescriptive → Cognitive
* 🔄 **Azure Data Factory:** Building secure, automated data pipelines and integrating on-prem data via Self-Hosted Integration Runtime (SHIR)
* 🧠 **Azure Machine Learning:** Applying AutoML and Designer to train, test, and explain models
* 📈 **Power BI Integration:** Visualizing machine learning outputs and KPI dashboards
* 🔐 **Security & Governance:** Firewalls, IP allow-lists, Azure AD, and compliance controls

---

## 🧩 End-to-End Demo Overview

**Use Case:** *Predicting customer subscription likelihood and identifying conversion factors.*

### Data Sources

* **MariaDB:** Marketing table — contact type, campaign data, duration, and subscription outcome
* **MySQL:** Profile table (age, job, education) & History table (loan, balance, housing, default)

### Data Pipeline (Azure Data Factory)

* Connects on-premise relational sources via **Self-Hosted Integration Runtime**
* Merges and transforms tables into a single, cleansed dataset (`input_prediction`)
* Loads into **Azure Synapse Analytics** for scalable processing

### Machine Learning (Azure ML)

* Uses **AutoML experiments** to test multiple models
* Achieved **~90% prediction accuracy**
* **Top features:** Call duration, month, and contact type strongly influence subscriptions

### Power BI Reporting

* Imports model outputs: `subscription_class` & `subscription_probability`
* Provides an interactive report with visualized KPIs
* **Key insights:**

  * Longer call durations → higher conversion likelihood
  * Ideal target age group: 30–40 years
  * Customers without loans → more likely to subscribe

---

## 🏗️ Reference Architecture

| Layer               | Tool                    | Purpose                                   |
| ------------------- | ----------------------- | ----------------------------------------- |
| **Source**          | MySQL / MariaDB         | Customer profile and marketing data       |
| **Ingestion & ETL** | Azure Data Factory      | Pipeline orchestration and transformation |
| **Storage**         | Azure Synapse Analytics | Central data warehouse                    |
| **ML Engine**       | Azure Machine Learning  | Model training and AutoML experimentation |
| **Visualization**   | Power BI                | Dashboard reporting & predictive insights |
| **Security**        | Azure AD / Firewalls    | Data protection and controlled access     |

---

## 🧪 Sample Use Cases

* 🧩 **Classification:** Customer churn and subscription prediction
* 🛒 **Recommendation Systems:** Market basket analysis and product suggestions
* 💬 **Sentiment Analysis:** NLP-based customer feedback monitoring
* 📅 **Time Series Forecasting:** Predicting sales, stock, or price trends

---

## 🔐 Key Q&A Takeaways

* **Can AI handle unstructured (petroleum/big) data?**
  Yes — with preprocessing, correlation mapping, and unstructured data mining using Azure ML.

* **How to connect on-prem databases to Azure?**
  Through **Self-Hosted Integration Runtime (SHIR)** in Azure Data Factory.

* **Can I secure cloud access?**
  Yes — configure **Azure Firewalls**, IP restrictions, and **Active Directory roles**.

* **Can models be built on-premise?**
  Yes, but cloud scaling is preferred for enterprise workloads.

---

## 🧱 Stack Summary

* **Languages:** Python, SQL
* **Core Services:** Azure Data Factory, Azure Synapse, Azure ML, Power BI
* **Data Types:** Structured (SQL), Semi-structured (JSON), Unstructured (optional)
* **Security:** Azure AD, Firewalls, Private Endpoints
* **Dev Environments:** Visual Studio, Jupyter, Databricks

---

## 🧭 Session Structure

1. Welcome & Introduction
2. Cloud BI Concepts & Value Proposition
3. Analytics Evolution (Descriptive → Cognitive)
4. Building a Cloud Data Pipeline
5. Machine Learning Workflow (Train → Evaluate → Explain)
6. Power BI Deployment & Visualization
7. Security & On-Prem Integration
8. Q&A and Closing Remarks

---

## 📚 Further Learning

* [Azure Data Factory Documentation](https://learn.microsoft.com/azure/data-factory/)
* [Azure Machine Learning Documentation](https://learn.microsoft.com/azure/machine-learning/)
* [Azure Synapse Analytics Documentation](https://learn.microsoft.com/azure/synapse-analytics/)
* [Power BI Documentation](https://learn.microsoft.com/power-bi/)

---

## 📬 Contact

**Presenter:** Jermaine Samuels
**Email:** [jc.samuels21@gmail.com](mailto:jc.samuels21@gmail.com)
**Organization:** Fujitsu Caribbean
**YouTube Session:** [https://www.youtube.com/watch?v=mWW-OsELCn0&t=1400s](https://www.youtube.com/watch?v=mWW-OsELCn0&t=1400s)

---

## 🏷️ Keywords

`Azure Data Factory`, `Azure Machine Learning`, `Power BI`, `Synapse Analytics`, `Business Intelligence`, `Data Engineering`, `AutoML`, `MLOps`, `Fujitsu Caribbean`, `Cloud Analytics`, `AI for BI`

---

## 📄 License

This README and session content are provided for educational and portfolio purposes.
© Jermaine Samuels — Fujitsu Caribbean. All rights reserved.

---

Would you like me to also include a short “**How to Add This to Your Portfolio**” section (e.g., embedding the YouTube thumbnail and GitHub badge for presentation)? It would make your GitHub page more visually engaging.
