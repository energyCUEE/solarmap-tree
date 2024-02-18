# Thailand Solar Irradiance Map: Analysis of Tree-based Models
Solar irradiance map project that provides analysis of tree-based models submitted to PMAP2024
<div align="center">
  <img width="500" alt="Screenshot 2567-02-18 at 20 37 05" src="https://github.com/energyCUEE/solarmap-tree/assets/113121308/97e1a9b4-9320-4415-a404-a945f847db07">
  <br>
  <p>Thailand Solar Irradiance Map</p>
</div>

This paper presents the methodology of estimat- ing global horizontal irradiance (GHI) across Thailand and displaying as a Thailand solar irradiance map available at https://www.cusolarforecast.com/. Estimates of GHI can be further used to approximate potential generated solar power at locations where only install capacity is known. The method uses geographical information, clear-sky irradiance, and cloud amounts from Himawari-8 satellite images as inputs for tree- based models to approximate the clear-sky index under the presence of cloud. Currently, the random forest model is being implemented on the platform. After acquiring more historical data, our assessment shows that the LightGBM model achieves improved accuracy in most cloud conditions.

Index Terms—solar irradiance estimation, random forest, extra tree, LightGBM

This repository consists of the following folders:

- `codes`
  - `lightgbm_PI_analysis.ipynb`: Analyzes the predictions of irradiance from the LightGBM model in a probabilistic sense.
  - `tree-based_model_training.ipynb`: Trains models that contain tree-based models using AutoML.
  - `tree-based_model_evaluation.ipynb`: Evaluates the tree-based model.

- `exp_results`
  - `graph_visualization.ipynb`: The notebook used to visualize the data.
  - `cross_valid_shorten.csv`: Results of model comparison from AutoML.
  - `lightgbm_test_result.csv`: Estimated irradiance from the LightGBM model in the test set.
  - `lightgbm_train_result.csv`: Estimated irradiance from the LightGBM model in the training set.
  - `Ihat_et_test_set.csv`: Estimated irradiance from the Extra Trees model in the test set.
  - `Ihat_lightgbm_v2_test_set.csv`: Estimated irradiance from the LightGBM v2 model in the test set.
  - `Ihat_rf_test_set.csv`: Estimated irradiance from the Random Forest model in the test set.


The input data can be accessed at: https://chula-my.sharepoint.com/:f:/r/personal/jitkomut_s_chula_ac_th/Documents/CHULA_solar_data/Himawari_processed_cloud/cloud_extraction_53stations?csf=1&web=1&e=ry6y80

## Contributors

1. **Suwichaya Suwanwimolkul**
   - Affiliation: Department of Electrical Engineering, Faculty of Engineering, Chulalongkorn University, Bangkok, Thailand
   - Email: [suwichaya.s@chula.ac.th](mailto:suwichaya.s@chula.ac.th)

2. **Wijarn Wangdee**
   - Affiliation: Center of Excellence in Electrical Power Technology, Chulalongkorn University, Bangkok, Thailand
   - Email: [wijarn.w@chula.ac.th](mailto:wijarn.w@chula.ac.th)

3. **Naebboon Hoonchareon**
   - Affiliation: Department of Electrical Engineering, Faculty of Engineering, Chulalongkorn University, Bangkok, Thailand
   - Email: [naebboon.h@chula.ac.th](mailto:naebboon.h@chula.ac.th) 

4. **Nuttamon Thungka**
   - Affiliation: Department of Electrical Engineering, Faculty of Engineering, Chulalongkorn University, Bangkok, Thailand
   - Email: [nuttamon.thungka@gmail.com](mailto:nuttamon.thungka@gmail.com)

5. **Natanon Tongamrak**
   - Affiliation: Center of Excellence in Electrical Power Technology, Chulalongkorn University, Bangkok, Thailand
   - Email: [natanon.t@chula.ac.th](mailto:natanon.t@chula.ac.th)

6. **Jitkomut Songsiri**
   - Affiliation: Department of Electrical Engineering, Faculty of Engineering, Chulalongkorn University, Bangkok, Thailand
   - Email: [jitkomut.s@chula.ac.th](mailto:jitkomut.s@chula.ac.th)


