"""
Change data isung re module
"""
# project imports
import re


def generate_message(res: str) -> str:
    """
    generate message
    :param res:str
    :return: str
    """
    res = list(res)
    count = 0
    for i in res:
        if i == None:
            res[count] = " "
        count += 1
    return (
            res[0]
            + "\n"
            + res[1]
            + "\n"
            + res[2]
            + res[3]
            + "\n"
            + res[4]
            + "\n"
            + res[5]
            + "\n"
            + res[6]
            + "\n"
            + format_birth(res[7])
            + format_wedding(res[8])
            + format_divorce(res[9])
            + format_death(res[10])
            + format_testament(res[11])
            + format_additional(res[12])
    )


def remove_new_lines(res: str) -> list:
    """
    remove new lines
    :param res:str
    :return: str
    """
    if res != None:
        new_res = []
        for r in res:
            new_r = re.sub(r"\s{2,}", " ", r)
            new_res.append(new_r)
        return new_res


def remove_forbidden_characters(res: str) -> list:
    """
    delete forbidden characters from string
    :param res: str
    :return: str
    """
    if res != None:
        new_res = []
        for r in res:
            new_r = re.sub(r"[`*]", " ", r)
            new_res.append(new_r)
        return new_res


def format_birth(birth: str) -> str:
    """
    change birth information
    :param birth: str
    :return: str
    """
    if birth != ";":
        birth = "*Метричні книги про народження*;" + birth
    if birth != None:
        birth = replace_semicolon_to_newline(birth)
        return (
                re.sub(
                    r"^\s?Метричні книги про народження;\s?(.*)$",
                    r"*Метричні книги про народження*",
                    birth,
                    flags=re.DOTALL,
                )
                + "\n"
        )


def format_wedding(wedding: str) -> str:
    """
    change wedding information
    :param wedding: str
    :return: str
    """
    if wedding != ";":
        wedding = "*Метричні книги про шлюб*;" + wedding
    if wedding != None:
        wedding = replace_semicolon_to_newline(wedding)
        return (
                re.sub(
                    r"^\s?Метричні книги про шлюб;:\s?(.*)$",
                    r"*Метричні книги про шлюб*",
                    wedding,
                    flags=re.DOTALL,
                )
                + "\n"
        )


def format_divorce(divorce: str) -> str:
    """
    change divorce information
    :param divorce: str
    :return: str
    """
    if divorce != None:
        divorce = replace_semicolon_to_newline(divorce)
        return divorce + "\n"


def format_death(death: str) -> str:
    """
    change death information
    :param death: str
    :return: str
    """
    if death != ";":
        death = "*Метричні книги про смерть*;" + death
    if death != None:
        death = replace_semicolon_to_newline(death)
        return (
                re.sub(
                    r"^\s?Метричні книги про смерть;:\s?(.*)$",
                    r"*Метричні книги про смерть*",
                    death,
                    flags=re.DOTALL,
                )
                + "\n"
        )


def format_testament(testament: str) -> str:
    """
    change testament information
    :param testament: str
    :return: str
    """
    if testament != None:
        testament = replace_semicolon_to_newline(testament)
        return (
                re.sub(
                    r"^\s?сповідні відомості:\s?(.*)$",
                    r"*сповідні відомості:*`",
                    testament,
                    flags=re.DOTALL,
                )
                + "\n"
        )


def format_additional(additional: str) -> str:
    """
    change additional information
    :param additional: str
    :return: str
    """
    if additional != None:
        additional = replace_semicolon_to_newline(additional)
        return additional + "\n"


def replace_semicolon_to_newline(string: str) -> str:
    """
    replace semicolon to new line
    :param string:str
    :return: str
    """
    if string != None:
        return string.replace(";", "\n")
