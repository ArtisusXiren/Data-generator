#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def func_format(products_data,missing_data,directory):
    import pandas as pd
    import os
    id_number=0
    temp_id=0
    file_to_store_x = ""
    title_filtered=[value for value in missing_data['Handle']]
    products_filtered=products_data[products_data['Title'].isin(title_filtered)]
    output_destination=os.path.join(directory,f"title_file_only")
    if not os.path.exists(f"{output_destination}.csv"):
        file_to_store_x=f"{output_destination}.csv"
        products_filtered.to_csv(file_to_store_x,index=False)
            
    else:
        temp_id+=1
        while os.path.exists(f"{output_destination}_{temp_id}.csv"):
            temp_id+=1
        id_number=temp_id
        file_to_store_x =f"{output_destination}_{id_number}.csv"
        products_filtered.to_csv(file_to_store_x, index=False)  
    id_number_x=0
    temp_id_x=0
    products_csv=pd.read_csv(file_to_store_x)
    products_handle=[value for value in products_csv['Handle']]
    products_final=products_data[products_data['Handle'].isin(products_handle)]
    products_duplicate=products_final[products_final.duplicated(subset='Handle', keep=False)]
    products_nonduplicates= products_final.drop_duplicates(subset='Handle', keep=False)
    final_result = pd.concat([products_duplicate, products_nonduplicates])
    new_file=os.path.join(directory,f"output_file")
    if not os.path.exists(f"{new_file}.csv"):
        file_to_store=f"{new_file}.csv"
        final_result.to_csv(file_to_store,index=False)
    else:
        temp_id_x+=1
        while os.path.exists(f"{new_file}_{temp_id_x}.csv"):
            temp_id_x+=1
        id_number_x =temp_id_x
        file_to_store=f"{new_file}_{id_number_x}.csv"
        final_result.to_csv(file_to_store, index=False)
    p_category={}
    new_list=[]
    for sku_id,label in zip(final_result['Variant SKU'],final_result['Handle']):
         if label not in p_category:
            p_category[label]=1
         else:
             p_category[label]+=1
         if sku_id is None:
            new_id=p_category[label]
            new_name_=f"{prev_id}_{new_id}"
            new_list.append(new_name)
         else:
            new_id=p_category[label]
            new_name=f"{sku_id}_{new_id}"
            new_list.append(new_name)
            prev_id=f"{sku_id}"   
       
    final_result['Variant SKU']=new_list
    P_file=os.path.join(directory,f"final_output_file")
    if not os.path.exists(f"{P_file}.csv"):
        final_result.to_csv(f"{P_file}.csv",index=False)
    else:
        temp_id_x+=1
        while os.path.exists(f"{P_file}_{temp_id_x}.csv"):
            temp_id_x+=1
        id_number_x =temp_id_x
        file_to_store=f"{P_file}_{id_number_x}.csv"
        final_result.to_csv(file_to_store, index=False)
   

    
