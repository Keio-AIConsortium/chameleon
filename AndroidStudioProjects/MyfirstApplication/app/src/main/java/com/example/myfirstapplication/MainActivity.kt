package com.example.myfirstapplication
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView
import java.io.BufferedReader
import java.io.InputStreamReader


class MainActivity : AppCompatActivity() {


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val minput = InputStreamReader(assets.open("stationData.csv"))
        val reader = BufferedReader(minput)

        var line : String
        var displayData :String =""
        while (reader.readLine().also{line = it} !=null){
            val row : List<String> = line.split(",")
        }

    }

}
