// HomeScreen.js
import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

const HomeScreen = ({ navigation }) => {
  const [companyName, setCompanyName] = useState('');
  const [description, setDescription] = useState('');
  const [motto, setMotto] = useState('');

  const handleGenerateSlogan = () => {
    // Pass the inputs as parameters to the next screen
    navigation.navigate('LoadingScreen', { companyName, description, motto });
  };

  return (
    <View style={styles.container}>
      <TextInput
        placeholder="Company Name"
        value={companyName}
        onChangeText={setCompanyName}
        style={styles.input}
      />
      <TextInput
        placeholder="Description"
        value={description}
        onChangeText={setDescription}
        style={styles.input}
      />
      <TextInput
        placeholder="Motto"
        value={motto}
        onChangeText={setMotto}
        style={styles.input}
      />
      <Button
        title="Generate Slogan"
        onPress={handleGenerateSlogan}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  input: {
    width: '100%',
    margin: 10,
    borderBottomWidth: 1,
    borderColor: 'gray',
    padding: 10,
  },
});

export default HomeScreen;
