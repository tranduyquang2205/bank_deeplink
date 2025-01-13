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
    url = "https://zpm.zalo.me/api/v1/transfer-money?api_key=3bb9d514148ca6dd16ba88d6bff387bf&data=B3F55D5CFD1E954F35410913B9A78792B932491314DA1E488E853E2AC0DA39D6B6B774B6FFF714E677ED73055903B0F48BD14929B320AA4AAE2F38ED3E2E538203E17875F3022781193E01A8356BD73B60FFFCBDBD03F834C03479999DA2BF46BC1848F3C751BDBFDD2ECA431CDA17259E26B67F1EA7B44568BA63C28BF16220D2FBA08653AB23E57848AD81330FA6E7CF2F588D82C1F988B3391A4EE660EE5328A31D97CCBAE3B37E7D1C990B5CD45FBB44495F182117A77932A4A7A24387DA7AE7088E9102327CA6D5923A5BAEA592CD9998450BC26AAA333CE997BF5F3D0FEE45B8C0188C06225340B95AFB76433EAC9B9E521FA0AF8CA6520E95C49F3E5E16447C39AD80EF4CCFF13D4818AFFCA24F7923FEAB6E0D40FE8BFBB2423D646231F8E177143D8A7CF5FA4044D1159BC00DEF3428222B98392835C5B1135525546E79AB9A8EBBEB308B07CCBE13BBB2F2AE55C45C5993BCECEE846C2DC827EFFB00F7D00E430DCF3C3D676868BC4C953D&encryptParams=1&sig=d16855427d230c0e9065eb388538ed08"
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