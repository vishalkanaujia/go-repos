package main

import (
	"fmt"

	"github.com/jinzhu/gorm"
	_ "github.com/lib/pq"
)

const (
	host     = "localhost"
	port     = 5432
	user     = "postgres"
	password = ""
	dbname   = "postgres"
)

type Setting struct {
	ID       int64     `sql:"auto_increment" json:"-"`
	Channels []Channel `json:"channel"`
}

type Channel struct {
	ID                int64  `sql:"auto_increment" json:"-"`
	ChannelID         string `json"id"`
	CommunicationMode string `json:"communication_mode"`
	Enabled           bool   `json:"enabled"`
	Type              string `json:"string"`
	//Groups []Group `json:"groups"`
	SettingID int64   `json:"setting_id"`
	Setting   Setting `gorm:"foreignkey:setting_id" json:"-"`
}

type Group struct {
	ID      int64  `sql:"auto_increment" json:"-"`
	GroupID string `json"id"`
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

	// Migrate the schema
	db.AutoMigrate(&Setting{})

	// Create
	db.Create(&Setting{
		Channels: []Channel{
			{
				ChannelID:         "1nc",
				Type:              "notification_channel",
				CommunicationMode: "push",
			},
		},
	})
}
