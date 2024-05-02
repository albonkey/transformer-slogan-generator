import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';

const SloganDisplayScreen = ({ route, navigation }) => {
  const { companyName, slogan } = route.params;

  return (
    <LinearGradient
      colors={['#4c669f', '#3b5998', '#192f6a']}
      style={styles.container}
      start={{ x: 0, y: 0 }}
      end={{ x: 1, y: 1 }}
    >
      <View style={styles.box}>
        <Text style={styles.title}>Company Name:</Text>
        <Text style={styles.value}>{companyName}</Text>
        <Text style={styles.title}>Slogan:</Text>
        <Text style={styles.value}>{slogan}</Text>
      </View>
      
      <TouchableOpacity style={styles.button} onPress={() => navigation.navigate('Home')}>
        <Text style={styles.buttonText}>Generate New Slogan</Text>
      </TouchableOpacity>
    </LinearGradient>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  box: {
    width: '90%',
    backgroundColor: 'white',
    borderRadius: 10,
    padding: 20,
    marginBottom: 20,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
  title: {
    fontSize: 18,
    color: '#333',
    fontWeight: 'bold',
    marginBottom: 5,
  },
  value: {
    fontSize: 16,
    color: '#555',
    marginBottom: 20,
  },
  button: {
    backgroundColor: '#e63946',
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 20,
  },
  buttonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: 'bold',
  },
});

export default SloganDisplayScreen;
