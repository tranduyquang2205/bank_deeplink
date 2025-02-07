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
    url = "https://zpm.zalo.me/api/v1/transfer-money?api_key=3bb9d514148ca6dd16ba88d6bff387bf&data=68ACB6D86189C5775E72D94B8B87C64D7709749BF25F3BF1D0BC6CC12B3B2AE3DCCBDA053B70F4FD0B24B96955067B9937A5159A16C3D806D77DCFEF590D5B103065A1F6C45D9AD416FC40CC86618F4923203F8147901C230467F11F08DFF15FE0AA2016BB28F8599CFF1AFFC2C1D74F6C0F97E577EE666D06526232579C8DEED117B88468873B671E2BF3909CD3A3CD3554A0D5B283B26E77017C8B46B8C17635ABF8322D6FCDAF28648E8D7ECABEF9D08E05192F808CEA98F33CCD028A892C316271878670EAD2C6A8756A9361DA283752BB7F90EFDD9E8E3BBF417E39A129A46136B2883557E504A0C56C721D1A13F1CB7FB91081A740B36857A8E5357D3EF3839A5DA2D72BC0A6857F9489D07C0342B969A1B27F2D341D9A3654866AB0ABA9BFF6ACA35B15D8A4E543283642B94B9C43F04B2374C03D57C913C2AD2346626C74D42EE3545F2C7B6AA4F09DB0ACACD357001AFE1DA6AD63630901043075F552F763E94D3B7DA29A0B7552EE391784&encryptParams=1&sig=0251bfab69a8bc248b84d6de5c14e71b"
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