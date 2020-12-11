package main

import (
    "fmt"
    "os"
    "strings"
)

func main() {
    argLen := len(os.Args)
    if argLen <= 2 {
        fmt.Println("USAGE: program.exe [encrypt/decrypt] [text]")
        os.Exit(0)
    }

    var mode string = os.Args[1]
    text := os.Args[2:]

    if mode == "encrypt" {
        join := strings.Join(text," ")
        var text Encryptor = []byte(join[:])
        fmt.Println(text.Encrypt())
    }


    if mode == "decrypt" {
        join := strings.Join(text," ")
        var text Decryptor = []byte(join[:])
        fmt.Println(text.Decrypt())
    }


}

type Encryptor []byte
type Decryptor []byte





//Using bytes instead of a string so we can encrypt things like images


func (s Encryptor) Encrypt() string {
    var buf string
    for _,v := range s {
        buf=buf+string(v+3)
    }
    return buf
}

//Add the Encrypt method too our type

func (s Decryptor) Decrypt() string {
    var buf string
    for _,v := range s {
        buf=buf+string(v-3)
    }
    return buf
}

//Add the Decrypt method too our type
