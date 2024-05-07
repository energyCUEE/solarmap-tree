import numpy as np
import pandas as pd

# to use these 2 functions, you have to create 'date' column and 'k' column
# 'date' obtain from concatenating of 'Datetime' and 'site_name'
# 'k' calculate from measurement of I and calculated clear-sky irradiance

def split_day_by_roc(df_site, threshold_k=0.7, spliting_k=0.6):
    all_date_list = list(set(df_site.index.date))
    clr_date_list = []
    partly_cloudy_date_list = []
    cloudy_date_list = []
    
    for date in all_date_list:
        date_df = df_site[df_site.index.date == date].copy()  # Create a copy to avoid SettingWithCopyWarnings
        date_df['is_increasing'] = (date_df['I'].diff() > 0).astype(int)

        date_df['is_concave_point'] = date_df['is_increasing'].diff()
        date_df['is_concave_point'] = date_df['is_concave_point'] == -1

        clr_condition = (np.sum(date_df['is_concave_point']) == 1) and (np.sum(date_df['k'] <= threshold_k) <= 0)
        partly_cloudy_condition = (date_df['k'].mean()) >= spliting_k

        if clr_condition:
            clr_date_list.append(date)
        elif partly_cloudy_condition:
            partly_cloudy_date_list.append(date)
        else:
            cloudy_date_list.append(date)

    return clr_date_list, partly_cloudy_date_list, cloudy_date_list
def split_train_test_sky_condition(updated_measurement_df, train_frac=0.6, random_state=42):  
    # Step 1: Cluster sky-condition 
    cluster_info_df = pd.DataFrame()

    for site_no in range(1, 57):
        site_name = f"ISL{('00' + str(site_no))[-3:]}"
        df_site = updated_measurement_df[updated_measurement_df['site_name'] == site_name].copy()
        df_site['Datetime'] = pd.to_datetime(df_site['Datetime'])
        df_site.set_index('Datetime', inplace=True)

        clr_date_list, partly_cloudy_date_list, cloudy_date_list = split_day_by_roc(df_site, threshold_k=0.7, spliting_k=0.6)

        cluster_df_site = pd.DataFrame({'Date': clr_date_list + partly_cloudy_date_list + cloudy_date_list,
                                        'site_name': [site_name] * len(clr_date_list + partly_cloudy_date_list + cloudy_date_list),
                                        'date': [f"{date} {site_name}" for date in clr_date_list + partly_cloudy_date_list + cloudy_date_list],
                                       'condition': ['clr']*len(clr_date_list) + ['partly_cloudy']*len(partly_cloudy_date_list)+['cloudy']*len(cloudy_date_list)})
        cluster_info_df = pd.concat([cluster_info_df, cluster_df_site], ignore_index=True)
        print(f"Finished clustering sky-condition of site {site_name}")

    # Step 2: Sampling train-test from each condition
    train_info_df = pd.DataFrame()
    test_info_df = pd.DataFrame()

    for condition in ['clr', 'partly_cloudy', 'cloudy']:
        condition_df = cluster_info_df[cluster_info_df['condition']==condition]
        condition_train_df = condition_df.sample(frac=train_frac, random_state=random_state)
        condition_test_df = condition_df.drop(condition_train_df.index)

        train_info_df = pd.concat([train_info_df, condition_train_df], ignore_index=True)
        test_info_df = pd.concat([test_info_df, condition_test_df], ignore_index=True)

    # Merge cluster information with the original DataFrame
    updated_measurement_df['is_train'] = updated_measurement_df['date'].isin(train_info_df['date'])
    
    # Separate train and test DataFrames
    train_df = updated_measurement_df[updated_measurement_df['is_train']]
    test_df = updated_measurement_df[~updated_measurement_df['is_train']]

    return train_df, test_df, train_info_df, test_info_df, cluster_info_df
