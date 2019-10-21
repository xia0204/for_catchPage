

def splitcookie(cookiess):

    cookies = [i.strip() for i in cookiess.split(";")]
    clist = []
    for i in cookies:
        k = i.split("=")
        clist.append({"name":k[0],"value":k[1]})
    # clist = [{"name":i.split("=")[0],"value":i.split("=")[1]} for i in cookiess ]
    return clist
def do_cookie(strc):
    cookie_dict = {i.split("=")[0]: i.split("=")[-1] for i in strc.split("; ")}
    return cookie_dict

if __name__ == "__main__":
    cookiestr = "JSESSIONID=444D33F3B336A9C5E135C639F41A42F1; tuNQaYE2WCOr8181S=vft23GDxVDyoL_mXEN_QONDRh56f45NMJ6mvEMRv9vBq_gU2qY1BI6Y7e7LOOre0; tuNQaYE2WCOrenable=true; tuNQaYE2WCOr8080S=8x57tJ_gDntTGKCWRhle96INke1k3aCubAUQfS.1rYldG4EIlBOsbuTDQm0yKBIB; tuNQaYE2WCOr8080T=4ZFFJ.claWl6PwegQBPPnIrUk2nFes.ixaonjUpBK0D6EsnxKAR4fDkZPjpQ9Ij5szDataLNfZhQtMfozIGAQxnE2vyQBXWx2G6_XKhBb7HkxXkrpwtwAZyV8spwtNWCvhmci_QDH3jvw52F1Ko6B9zZsC17myD.dokg0PAg.fzwVGZ1lvPufCnyyXixJ1rcy4V1mtVqKqo8VZzynub8SECzgg6oXzVP76jX_C0gJprMBPaKafpWzjdcajyPwQNFx8KtUaQ4nO9z.2nsG.jpsUW.E.wLt0jqBTEQ6R0qKAT4_AJi2tXHoyAkKXc_.vM8.Ib1vrdPHvrxyMzzezOj.N9.sY1A4gVK5B5UOWaXWK3_3Wq; JSESSIONID=628D7207E892FF91EAE285B2B84DB5E0; tuNQaYE2WCOr8181T=4KvIglg7I4FbycJ7G7vDe3vXcrh6tL_xHNxt5QFC.Ru7XTtF9_42eBJQrwe9X_GvNkcycY25Uernvm0jZKzZLllfMyrhqQtKHFkH0fczNGo2MLvM57qyIxu85PFpqlnvrG4Ze7Dkk8KhxJwVOraC8fhO2kWLdZqWT.0TSV8BDGyI6Xv6WeI10wiNFa_0w07.JXcU45N4kbqU4sek_Cm7Wvi43LyoHI0B1K6B_Jb278r0_0F0kfSwOgzUewOQylJnAxh7sQNSSdS_blqX2wm_xz0GOcar4TeWsRluFL1hzt.7sBdr5ZwXe.IK8f2kSJOwbi4NjxjvQNgMI4li9mKE.mwD_vCZOarMJMvOa0IS9q6ocba"
    cookiestr1 = "	ASP.NET_SessionId=5erhd4bmu5lrjfl3yi0w1tgh; WeixinInstalledFlag=3TxCjc4NofM=; a7b=GI2psMTYn2Y=; safedog-flow-item=; Hm_lvt_e9fbb032b10c5c15b56785253103246f=1570596079; Hm_lpvt_e9fbb032b10c5c15b56785253103246f=1570596079"
    # for i in splitcookie(cookiestr1):
    #     print(i)
    print(do_cookie(cookiestr1))