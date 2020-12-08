import re


def validate_byr(byr):
    byr = int(byr)
    if not (1920 <= byr <= 2002):
        raise Exception


def validate_iyr(iyr):
    if not (2010 <= iyr <= 2020):
        raise Exception


def validate_eyr(eyr):
    if not (2020 <= eyr <= 2030):
        raise Exception


def validate_hgt(hgt):
    cm_match = re.compile(r"^\d+(?=cm$)").search(hgt)
    in_match = re.compile(r"^\d+(?=in$)").search(hgt)
    if cm_match:
        cm_hgt = int(cm_match[0])
        if not (150 <= cm_hgt <= 193):
            raise Exception
    elif in_match:
        in_hgt = int(in_match[0])
        if not (59 <= in_hgt <= 76):
            raise Exception
    else:
        raise Exception


def validate_hcl(hcl):
    hcl_match = re.compile(r"^#[a-f0-9]{6}$").search(hcl)
    if not hcl_match:
        raise Exception


def validate_ecl(ecl):
    ecl_match = re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$").search(ecl)
    if not ecl_match:
        raise Exception


def validate_pid(pid):
    pid_match = re.compile(r"^\d{9}$").search(pid)
    if not pid_match:
        raise Exception
