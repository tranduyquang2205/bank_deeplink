import requests
import json

def save_dict_to_json(data_dict, file_path):
    """
    Save a dictionary to a JSON file.

    Args:
        data_dict (dict): The dictionary to save.
        file_path (str): Path to the output JSON file.

    Returns:
        None
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data_dict, json_file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Failed to save dictionary to JSON file: {e}")




def generate_deep_link(rec_bin,rec_acc_num,amount,msg,send_bin):
    url = "https://zpm.zalo.me/api/v1/transfer-money?api_key=3bb9d514148ca6dd16ba88d6bff387bf&data=317BE7295049D8EE5898ACC29296ABFFA17F01D320D1DDE55F82F814D681B2C35472A4ABB01378D6C37116AB729C7EBF924B99DE76E656405A3B3B24E78DA55C952E87EA26A0EF66DBAE40A581A1B44EF05C95D685B45D3980A49CC3BA8C7BC5882CC6C7FF14642105005B9DFF25EEE289B1A694443866B0FA5320A94EC3AD27CEDD7226EA0977EEA82952683C02FA9392D38D9BD68DA269C4E40D27F15834F2BACB18AB68AB26CBD46512C37AC23C4381875E0534B2257AB6637D4AD4C7719AB62F3851A47B6B87CF85355DE7F498BB674D95C99544940108AD7F71B6D4952B70EB4722CC468071C8056C468489BD30CF4081954861762D2E7C67608C042E6DD12B0C9CB3DC957822F86280E9E0A5CCA3D75272F5615A3BC1875745C879C45DE1FF85EC136A735C85E4F7DC092CC5ECAF71244DFC3B8595E92BCE44EB38CAC54A73A49578F6D5AB52DFF101CDB1F027ACF3715C0FF1B33E5C29C417B1267863&encryptParams=1&sig=c9fc2f049440f383c2f4bcbdb263be65"
    # Example usage
    payload_dict = {
        "rec_bin": rec_bin,
        "rec_acc_num": rec_acc_num,
        "rec_type": "1",
        "rec_method": "1",
        "srcId": "2",
        "amount":amount,
        "msg": msg,
        "send_method": "1",
        "send_bin": send_bin,
        "cateId": "1",
        "save_info": "false"
    }

    save_dict_to_json(payload_dict, "file.json")
    payload = {}
    files=[
    ('file',('file.json',open('file.json','rb'),'application/json'))
    ]
    headers = {
    'Accept-Encoding': 'gzip',
    'Connection': 'keep-alive',
    'User-Agent': 'Zalo/241002 (iPhone; iOS 18.1; Scale/3.00)',
    'Accept-Language': 'vi-VN;q=1, en-VN;q=0.9',
    'Cookie': 'zsid=rFLn.376070473.279.wzdwLNIyAUeztKFyTBmfwjz4Y_Pql2dgTJeKqnE_AUDql2dPGuePtKI87jb_l1jV; __zi=3000.SSZzejyD4iicchMgpau7W6gUigZ9Iak5Qfx_gCvDJeLjcFcj.1; _ga=GA1.1.1897660568.1730816329; _ga_LSB83G80DR=GS1.1.1731104417.2.0.1731104417.0.0.0; zalo.me_zacc_session=7eUExoGyu2PpffZtDZ3bFssDbjfZDl0S7OkrnWS5oIvTluVfBnt3Es-0Xk8C0F810xcHmoacvnmpiTlC2GUr0LWDSyn8Wm4a6pPcG8QzDxRC5X0jeRSfqSaiCqN2eIwC_2SLJV_25SZa361iYz98xYRApgbV80toDm; zalo.me_zapp=1566743541235789049; zalo.me_zlink3rd=v2_ARh6oVaO8AcChtuP60RVKQk6eXmzjAtXwoYDHEn4/RLBhew8nOouHovPNqv1RK5pzkWgRTX/5fXfWbfFSZTUKYCdj6+v/GpDOA5zGfYu5JA=; znid=600315016085584128; znuid_wg=N5vnqy5OFz5OCG6MYaC__1HDS_2FIZpt44rrzOb8F_Wo',
    'Host': 'zpm.zalo.me',
    'Accept': '*/*',
    'session_key': 'b6OO.376070473.a1.dUmY4F9mhpgx4SKiyd2lEl9mhphoSAywyrXB29KFhpe',
    'Upload-Draft-Interop-Version': '6',
    'v': 'v2',
    'zcid': 'A9E8CF5E6A949A34930583C47A79B90B2F27FA89D452473512C4631C86DB99E5416B330A726794BD9C430AFFF7D8E87B6F43F8B3428486DAB2430DC57AAC9B4DAF364EC61E01AD638FFB1782298F347B',
    'Upload-Complete': '?1',
    'retry': '0'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    try:
        response = response.json()
    except:
        response = response.text
    return response


rec_bin = "970457"
rec_acc_num = "902021186707"
amount = "60000000"
msg = "QRILU9229743678SVND5C1V"
send_bin = "970422"
generate_deep_link(rec_bin,rec_acc_num,amount,msg,send_bin)