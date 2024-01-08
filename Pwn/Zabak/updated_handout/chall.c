#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/sendfile.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdint.h>
#include <unistd.h>
#include <grp.h>

bool zaba_pripravena = false;
int pocet_drepu_v_rozcvicce = 0;
char zaba_opravdu_pripravena = 'N';
bool jazyk_rozcvicen = false;
bool utok_zahajen = false;

char *kameny[5] = {
    (char*)0xdeadbeef,
    (char*)0xdeadbeef,
    (char*)0xdeadbeef,
    (char*)0xdeadbeef,
    (char*)0xdeadbeef,
};

const char *frogs = "              _         _\n\
  __   ___.--'_`.     .'_`--.___   __\n\
 ( _`.'. -   'o` )   ( 'o`   - .`.'_ )\n\
 _\\.'_'      _.-'     `-._      `_`./_\n\
( \\`. )    //\\`         '/\\\\    ( .'/ )\n\
 \\_`-'`---'\\__,       ,__//`---'`-'_/\n\
  \\`        `-\\         /-'        '/\n\
   `                               '   VK";

void udelat_drep() {
    pocet_drepu_v_rozcvicce++;
    puts("A raz a dva");
}

void opravdu_pripravit_zabu() {
    zaba_opravdu_pripravena = 'Y';
    puts("Vždy připraven");
}

void protahnout_nohy() {
    zaba_pripravena = true;
    puts("Nohy protaženy");
}

void zahajit_utok() {
    utok_zahajen = true;
    puts("Zahajujeme útok! Mouchy, utečte!");
}

void rozcvicit_jazyk() {
    jazyk_rozcvicen = true;
    puts("Drbu vrbu, drbu vrbu");
}

void skok1() {
    kameny[0] = getenv("FLAG");
    if (!zaba_pripravena) {
        puts("Nejdříve se musíš protáhnout");
        exit(1);
    }
}

void skok2() {
    kameny[1] = kameny[0];
    if (pocet_drepu_v_rozcvicce < 42) {
        puts("Nezapomeňme na dřepy!");
        exit(1);
    }
}

void skok3() {
    kameny[2] = kameny[1];
    if (zaba_opravdu_pripravena != 'Y') {
        puts("Jsme opravdu dobře protažení?");
        exit(1);
    }
}

void skok4() {
    kameny[3] = kameny[2];
    if (!jazyk_rozcvicen) {
        puts("Jazyk ještě není rozcvicený");
        exit(1);
    }
}

void skok5() {
    kameny[4] = kameny[3];
    if (!utok_zahajen) {
        puts("Útok nebyl zahájen");
        exit(1);
    }
}

void moucha_ulovena() {
    if ((size_t)kameny[4] == 0xdeadbeef) {
        puts("Ale ale, nerozcvičená žába přece nemůže dostat vlajku...");
        exit(1);
    }
    if (kameny[4] == NULL) {
        puts("Tady by měla být vlajka. Prosím kontaktuj organizátory :(");
        exit(1);
    }
    puts("Gratuluju, moucha ulovena, tady je vlajka!");
    printf("FLAG: %s\n", kameny[4]);
    puts("Brzy naviděnou!");
    exit(0);
}


int main() {
    // dropping buffering
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);

    // dropping perms
    setgroups(0, NULL);
    setgid(1337);
    setuid(1337);

    puts(frogs);
    puts("       === ŽABÁK ===");
    puts("Žabák skáče po programu, a když bude skákat správně získá i vlajku!");

    size_t pointer = (size_t)protahnout_nohy;
    while (true) {
        printf("Kam si dnes žabák skočí?\n");
        printf("Pointer address: %zx\n", pointer);
        if (fread(&pointer, sizeof pointer, 1, stdin) != 1) {
            puts("Ups, tak to byl nepovedený skok :(");
            exit(1);
        }
        // ela hop!
        ((void (*)())pointer)();
    }
}
