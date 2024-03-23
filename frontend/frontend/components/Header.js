import React, {useState} from 'react';
import { SafeAreaView, View, StyleSheet, Text } from 'react-native';

export default function Header(){
  return(
    <SafeAreaView style={styles.header}>
      <Text style={styles.title}>Menu</Text>
    </SafeAreaView>
  )
}

const styles=StyleSheet.create({
  header:{
    height:60,
    paddingTop: 15,
    backgroundColor:'orange'
  },
  title:{
    textAlign:'center',
    color:'white',
    fontWeight:'bold',
    fontSize: 25
  }
})