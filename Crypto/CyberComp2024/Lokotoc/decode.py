from pwn import xor
import binascii
import base64

with open("./Crypto/CyberComp2024/Lokotoc/output2.txt") as f:
    encrypted_flag = binascii.unhexlify(f.readline().strip())
    encrypted_test = binascii.unhexlify(f.readline().strip())
    test_string = b"devadesatsest to je fakt krasne cislo ale ja musim vymyslet smysluplny text abych dokazal napravit chyby vseho co delam tohle je hrozne random a uz ani nevim co mam psat alespon si to trosku procvicim abych dostal tu zasranou vlakju ale na to aby tohle stacilo tak musim napsat alespon tri tisice znaku Sest tisicdvestedevadesatsest to je fakt krasne cislo ale ja musim vymyslet smysluplny text abych dokazal napravit chyby vseho co delam tohle je hrozne random a uz ani nevim co mam psat alespon si to trosku procvicim abych dostal tu zasranou vlakju ale na to aby tohle stacilo tak musim napsat alespon tri tisice znaku Sest tisicdvestedevadesatsest to je fakt krasne cislo ale ja musim vymyslet smysluplny text abych dokazal napravit chyby vseho co delam tohle je hrozne random a uz ani nevim co mam psat alespon si to trosku procvicim abych dostal tu zasranou vlakju ale na to aby tohle stacilo tak musim napsat alespon tri tisice znaku Sest tisicdvestedevadesatsest to je fakt krasne cislo ale ja musim vymyslet smysluplny text abych dokazal napravit chyby vseho co delam tohle je hrozne random a uz ani nevim co mam psat alespon si to trosku procvicim abych dostal tu zasranou vlakju ale na to aby tohle stacilo tak musim napsat alespon tri tisice znaku Sest tisicdvestedevadesatsest to je fakt krasne cislo ale ja musim vymyslet smysluplny text abych dokazal napravit chyby vseho co delam tohle je hrozne random a uz ani nevim co mam psat alespon si to trosku procvicim abych dostal tu zasranou vlakju ale na to aby tohle stacilo tak musim napsat alespon tri tisice znaku Sest tisicdvestedevadesatsest to je fakt krasne cislo ale ja musim vymyslet smysluplny text abych dokazal napravit chyby vseho co delam tohle je hrozne random a uz ani nevim co mam psat alespon si to trosku procvicim abych dostal tu zasranou vlakju ale na to aby tohle stacilo tak musim napsat alespon tri tisice znaku Sest tisicdvestedevadesatsest to je fakt krasne cislo ale ja musim vymyslet smysluplny text abych dokazal napravit chyby vseho co delam tohle je hrozne random a uz ani nevim co mam psat alespon si to trosku procvicim abych dostal tu zasranou vlakju ale na to aby tohle stacilo tak musim napsat alespon tri tisice znaku Sest tisicdvestedevadesatsest to je fakt krasne cislo ale ja musim vymyslet smysluplny text abych dokazal napravit chyby vseho co delam tohle je hrozne random a uz ani nevim co mam psat alespon si to trosku procvicim abych dostal tu zasranou vlakju ale na to aby tohle stacilo tak musim napsat alespon tri tisice znaku Sest tisicdvestedevadesatsest to je fakt krasne cislo ale ja musim vymyslet smysluplny text abych dokazal napravit chyby vseho co delam tohle je hrozne random a uz ani nevim co mam psat alespon si to trosku procvicim abych dostal tu zasranou vlakju ale na to aby tohle stacilo tak musim napsat alespon tri tisice znaku Sest tisicdvestedevadesatsest to je fakt krasne cislo ale ja musim vymyslet smysluplny text abych dokazal napravit chyby vseho co delam tohle je hrozne random a uz ani nevim co mam psat alespon si to trosku procvicim abych dostal tu zasranou vlakju ale na to aby tohle stacilo tak musim napsat alespon tri tisice znaku Sest tisicdvestedevadesatsest to je fakt krasne cislo ale ja musim vymyslet smysluplny text abych dokazal napravit chyby vseho co delam tohle je hrozne random a uz ani nevim co mam psat alespon si to trosku procvicim abych dostal tu zasranou vlakju ale na to aby tohle stacilo tak musim napsat alespon tri tisice znaku"

key_stream = xor(encrypted_test, test_string)

flag = xor(key_stream, encrypted_flag)[: len(encrypted_flag)]

for _ in range(15):
    flag = base64.b64decode((flag))

print(f"{flag=}")