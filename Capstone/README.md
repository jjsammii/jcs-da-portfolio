
# 🧠 Multimodal Glioma Segmentation and Classification Using Deep Learning

### 🎓 Master’s Capstone Project — MSc. Data Science, University of the West Indies

**In collaboration with:** Faculty of Medical Sciences, University Hospital of the West Indies
**Author:** Jermaine Samuels
**Date:** August 2021

---

## 🧩 Project Overview

This project presents an AI-driven system for **automated segmentation and classification of brain gliomas** (tumors) from MRI scans — distinguishing between **High-Grade Gliomas (HGG)** and **Low-Grade Gliomas (LGG)**.

Leveraging the **BraTS 2019 dataset**, the study implements a deep learning pipeline composed of **Convolutional Neural Networks (CNNs)** for medical image segmentation and classification, and an **NLP module** to mine trends from neuro-oncology literature.

This work was completed as part of the MSc. Data Science capstone project at the **University of the West Indies**, in collaboration with a **Medical Science graduate researcher** from the University Hospital of the West Indies.

---

## 🎯 Research Objectives

* Develop an end-to-end pipeline for **MRI-based glioma segmentation and classification** using CNN architectures.
* Apply **transfer learning** and **feature extraction** to compensate for limited annotated medical datasets.
* Integrate **NLP techniques** for knowledge discovery across brain tumor research publications.
* Provide a **visual dashboard** for model predictions and insights.

---

## 🧠 Project Components

| Notebook                               | Function                                                                  | Dataset            | Output                          |
| -------------------------------------- | ------------------------------------------------------------------------- | ------------------ | ------------------------------- |
| **Image Processing.ipynb**             | MRI preprocessing, `.nii` to `.png` conversion, and dataset organization. | BraTS 2019         | Cleaned data folders            |
| **Colab_Brats2019_Segmentation.ipynb** | Trains CNN segmentation (UNet-like) for tumor localization.               | BraTS 2019         | `BraTs2019mri_final_seg1.h5`    |
| **bratsclass_final.ipynb**             | CNN classifier for HGG vs LGG using transfer learning (ImageNet).         | Training/Test sets | `brats2019_imagenet_class.h5`   |
| **Test on Images.ipynb**               | Model evaluation on unseen patient MRIs.                                  | `/Patients`        | Accuracy and prediction reports |
| **Bratsmri_Dashboard.ipynb**           | Voila-based web dashboard for visualization and exploration.              | Local model        | Interactive dashboard           |
| **NLP.ipynb**                          | Literature mining with `pypaperbot` and keyword frequency analysis.       | Research articles  | Trend analysis plots            |

---

## ⚙️ Tech Stack

* **Languages:** Python (TensorFlow, Keras, PyTorch)
* **Libraries:** NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn
* **Deep Learning:** CNNs, Transfer Learning (VGG16, ResNet), AutoML tuning
* **NLP Tools:** NLTK, WordNet, pypaperbot
* **Visualization:** Power BI, Voila Dashboard
* **Dataset:** [BraTS 2019 — Brain Tumor Segmentation](https://www.kaggle.com/aryashah2k/brain-tumor-segmentation-brats-2019)

---

## 📊 Results Summary

* **Segmentation Accuracy:** ~90% Dice Similarity Coefficient
* **Classification Accuracy:** 91% test accuracy (HGG vs LGG)
* **Model Insight:** Tumor region morphology and call duration of MRI slices were primary features for accurate classification.
* **NLP Finding:** Peak publication activity 2018–2020, with “3D CNN” and “transfer learning” emerging as leading research trends.

---

## 📚 Literature Review

In most documented implementations of segmentation and classification of Gliomas, **MRIs** are selected as the preferred imaging source for machine learning using **Convolutional Neural Networks (CNNs)**. CNNs are promising because they are more reliable than traditional *a priori* or theoretical deductions dependent on human experts. Deep learning models, unlike traditional ones, do not require pre-selection and can automatically learn which features are most relevant for classification or prediction (Madeleine M. Shaver et al., 2021).

While CNNs have advanced glioma detection and classification significantly, they require large annotated medical datasets — which are scarce — and are sensitive to initialization parameters. Common mitigations include **analyzing 2D slices** instead of 3D volumes, **transfer learning**, and **feature extraction**.
When comparing CNNs to traditional methods, deep learning excels because it adapts dynamically when exposed to new data through hierarchical feature abstraction, surpassing human bias or predefined expert rules. In general, CNN accuracy in glioma classification exceeds **90%**.

The **classification** process of gliomas (grades I–IV) is informed by phenotypic expressions of malignant or atypical cell genetics. Tumor differentiation by pathologists relies on visual inspection of histopathology slides.
There are three histological glioma types: **astrocytoma**, **oligodendroglioma**, and **oligoastrocytoma** (Ertosun & Rubin, 2015).

* *Astrocytoma* arises from star-shaped supportive brain cells.
* *Oligodendroglioma* originates in the central nervous system (brain or spinal cord).
* *Oligoastrocytoma* represents a mix of both.

Diffuse gliomas are classified as per (Vigneswaran et al., 2015). The **1p/19q co-deletion** of chromosomes is a genetic marker for oligodendrogliomas, accounting for ~10–15% of adult diffuse gliomas (OncologyPRO).
Detecting these **phenotypic genetic features** is essential for accurate tumor grading, achieved via CNNs that extract spatial and textural information not easily recognized by humans.

From a computational perspective:

* **2D CNNs** analyze individual MRI slices for higher fidelity but lose contextual neighborhood data.
* **3D CNNs** incorporate volumetric continuity for better spatial understanding but demand higher compute and memory resources.
  According to Banerjee et al. (2020), classifying tumors from smaller 2D image patches enables CNNs to focus on localized tumor regions, minimizing irrelevant context but potentially missing volumetric cues.

**Segmentation**, typically performed using CNN architectures such as **U-Net**, is validated with **Dice** or **Sørensen** coefficients that measure overlap between predicted and actual tumor regions (Dice ≈ 1 ⇒ perfect overlap).
High segmentation accuracy correlates strongly with improved diagnosis, prognosis, and treatment planning. Enhancements arise from normalization of brain regions, modeling, and isolating **phenotypic subregions**—necrosis, edema, non-enhancing, and enhancing tumor tissue.

### Conclusion

Convolutional Neural Networks remain the foundation for glioma segmentation and classification, essential for distinguishing tumor tissue from healthy brain matter and assessing phenotypic variance across grades.
While 3D multimodal data offers depth, **2D feature extraction often yields greater fidelity** due to higher data density (e.g., 155 2D slices ≈ 1 3D scan).

### References

1. Shaver, M. M., Kohanteb, P. A. (2021). *Optimizing Neuro-Oncology Imaging: A Review of Deep Learning*. [MDPI Cancers, 11(6), 829](https://www.mdpi.com/2072-6694/11/6/829/pdf).
2. Ertosun, M. G., & Rubin, D. L. (2015). *Automated Grading of Gliomas Using Deep Learning in Digital Pathology Images*. [AMIA Symposium Proceedings](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4765616/).
3. Vigneswaran, K., Neill, S., & Hadjipanayis, C. G. (2015). *Beyond the WHO Grading of Infiltrating Gliomas: Advances in Molecular Genetics*. [Annals of Translational Medicine](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4430738/).
4. OncologyPRO. *1p/19q Co-Deletion in Glioma*. [ESMO Biomarker Factsheet](https://oncologypro.esmo.org/education-library/factsheets-on-biomarkers/1p-19q-co-deletion-in-glioma).
5. Banerjee, S., Mitra, S., Masulli, F., & Rovetta, S. (2020). *Glioma Classification Using Deep Radiomics*. [SN Computer Science](https://link.springer.com/article/10.1007/s42979-020-00214-y).

---

## 🧮 Dashboard Visualization

Launch the interactive dashboard to visualize predictions and keyword trends:

```bash
voila Bratsmri_Dashboard.ipynb
```

---

## 📄 Included Reports

* **Technical Report (PDF)** — Algorithm design and evaluation metrics.
* **Software Artefact Document (PDF)** — Detailed architecture, system dependencies, and workflow.
* **Management Report (PDF)** — Executive summary of project outcomes and implementation roadmap.

---

## 🔗 References & Resources

* Dataset: [BraTS 2019 Brain Tumor Segmentation](https://www.kaggle.com/aryashah2k/brain-tumor-segmentation-brats-2019)
* Supplementary Project Materials: *(included in repository)*

---

## 👨🏾‍💻 Author

**Jermaine Samuels**
MSc. Data Science, University of the West Indies
📧 [jc.samuels21@gmail.com](mailto:jc.samuels21@gmail.com)
🔗 [GitHub Portfolio](https://github.com/jjsammii)

---

Would you like me to add a **“Setup and Reproducibility Guide”** section (detailing how to recreate the training and dashboard environments using Anaconda or Docker)? That would make this repository fully replicable for research/public viewers.
