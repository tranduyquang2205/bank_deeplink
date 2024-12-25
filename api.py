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
    url = "https://zpm.zalo.me/api/v1/transfer-money?api_key=3bb9d514148ca6dd16ba88d6bff387bf&data=D6B964A63FAFB6ED42F76DE45ED99265D8914C9A850C9E70F50C53F23F233BA0B1EECB25E1D2A392DBADF6E1D94F912E4E3CC8781C9F92382C358BDDB9CF43231692B4FAF8894FF8691575E00D3EEA26EAD0FFF7CB54C803313430C71F048D5BD659EDC22A9A3DCDFCBB9177D16E49A6E572EF2AC9E88A0F2E67F7042C3F1ACE1A68541B29BCEF6291D0B1C39B0652A5CF33DC4C21E4E5E112787FD7FA18D3AC87E542D5C41FF039414D35FE1AA4B49A2CBBC3C1ED3AF2B7C57373FD2ABB9CC0841CE3CC7F80F0D71B82FDD374D8051D314D1B70FBDD17EEFDF00DEBDDAAC72020A4D18E9AFA38B38C320EED6853CC474FE70E2413A5C8F5C91B68B5CD57C93CBF7B99FD82E9236FB376DBEF1ABC44BEE9A3EBF55D52072A8A74827548C1BF5AA8C7C9077392D6000ED88C58437D28E1C4DA2C738EE3C53AB3FB4B7977A5E41379705619ADC1FE0A943A3669B79F3D1E05E61F585F81EBD21549127F7237E622309823A27E7D61A75621FA62B577F79D&encryptParams=1&sig=19671410df13b4cf6002148cc0efb01b"
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
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip',
    'Content-Length': '380',
    'Cookie': '__zi=3000.SSZzejyD4iicchMgpau7W6gUigZ9Iak5QfxxgSr1HuPgaV2k.1; zalo.me_zacc_session=hn4quVmouGB2C2BvxZxa6zmRBDIxEF4uh1qFoDyBo0hiAJtdznF27zuMEEtN0lecjIOYplOXxpk5BcZ1rW2z9kxcsOMNy117hORYGT-L29tyffGi-9yM-lcSjqIRYH6dp9UHJARgAkFKlEHjqlftnIQZLX9r-0Fp4m; zalo.me_zapp=1566743541235789049; zalo.me_zlink3rd=v2_ARh6oVaO8AcChtuP60RVKQk6eXmzjAtXwoYDHEn4/RKzH5Nfjj6c7XnGhtSHiVB2WpKg5qDoz5akeAQldMizcYsEz59j3oQbm+8UhuhtxZw=; znid=600315016085584128; znuid_wg=N5vnqy5OFz5OCHI7kMezxIPiTkozQpZf9snmwBjfEEyt; zsid=csuw.376070473.297.EghVsZ9DRnjxB0KDCarl6vcq-FyoJMyRCnqcSLLERn8oJMye1NjVB09vM2WvJMEp; _ga=GA1.1.1897660568.1730816329; _ga_LSB83G80DR=GS1.1.1735019291.2.1.1735019743.0.0.0; zalo.me_isoCode=vn; zalo.me_zidnbaid=3349332778580714293',
    'Host': 'zpm.zalo.me',
    'Accept': '*/*',
    'User-Agent': 'Zalo/241002 (iPhone; iOS 18.2; Scale/3.00)',
    'Accept-Language': 'vi-VN;q=1, en-VN;q=0.9',
    'zcid': 'A9E8CF5E6A949A34930583C47A79B90B2F27FA89D452473512C4631C86DB99E5416B330A726794BD9C430AFFF7D8E87B6F43F8B3428486DAB2430DC57AAC9B4DAF364EC61E01AD638FFB1782298F347B',
    'retry': '0',
    'Upload-Draft-Interop-Version': '6',
    'v': 'v2',
    'session_key': 'Th08.376070473.a1.kN3J2BLuw3By6O8ajNZeChLuw3ArUEWojBYrMD9uw38',
    'Upload-Complete': '?1'
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
print(generate_deep_link(rec_bin,rec_acc_num,amount,msg,send_bin))