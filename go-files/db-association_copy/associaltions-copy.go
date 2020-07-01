package main

import (
	"encoding/json"
	"fmt"

	"github.com/jinzhu/gorm"
	"github.com/jinzhu/gorm/dialects/postgres"
	_ "github.com/lib/pq"
)

const (
	host     = "localhost"
	port     = 5432
	user     = "postgres"
	password = ""
	dbname   = "guru"
)

type AllSettings struct {
	ID      int64     `sql:"auto_increment" json:"-"`
    EnLanguage postgres.Jsonb `json:"en"`
}

type Obj struct {
	Title string `json:"title"`
	Description string `json:"description"`
}

type NewVideo struct {
	Movie Obj`json:"movie"`
	Episode Obj `json:"episode"`
}

type PushObj struct {
	NewVideo NewVideo `json:"new_video"`
	
}

func main() {
	psqlInfo := fmt.Sprintf("host=%s port=%d user=%s "+
		"password=%s dbname=%s sslmode=disable",
		host, port, user, password, dbname)

	db, err := gorm.Open("postgres", psqlInfo)
	if err != nil {
		panic(err)
	}
	defer db.Close()


	push := `{
		  "new_video": {
			"movie": {
			  "title": "%s",
			  "description": "Available now!"
			},
			"episode": {
			  "title": "%s",
			  "description": "Episode %s: Available now!"
			}
		  }
	  }`

	db.AutoMigrate(&AllSettings{})

	var as AllSettings
	as = AllSettings{
		EnLanguage: postgres.Jsonb{json.RawMessage(push)},
	}

	db.Create(&as)

	var as1 AllSettings
	//db.First(&as1)
	db.Find(&as1)
	//fmt.Println(as1)

	var pushObj PushObj
	
	a, err := json.Marshal(as1.EnLanguage)
	err = json.Unmarshal(a, &pushObj)
    
	n := len(a)   //Find the length of the byte array
	s := string(a[:n]) //convert to string
	fmt.Println(pushObj.NewVideo.Episode)
    fmt.Printf(s, "a new show", "a new episode", "a new description") //write to response
}
